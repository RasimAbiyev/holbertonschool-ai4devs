import ast
from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewIssue:
    line: int
    severity: str
    rule: str
    message: str


class ReviewAnalyzer(ast.NodeVisitor):
    """Detect common Python code quality and security issues."""

    SUBPROCESS_FUNCTIONS = {
        "run", "Popen", "call", "check_call", "check_output"
    }

    def __init__(self):
        self.issues = []
        self.subprocess_aliases = set()
        self.subprocess_function_aliases = set()
        self.pickle_aliases = set()
        self.pickle_function_aliases = set()

    def add_issue(self, node, severity, rule, message):
        self.issues.append(
            ReviewIssue(
                line=getattr(node, "lineno", 1),
                severity=severity,
                rule=rule,
                message=message,
            )
        )

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name == "subprocess":
                self.subprocess_aliases.add(
                    alias.asname or "subprocess"
                )
            elif alias.name == "pickle":
                self.pickle_aliases.add(
                    alias.asname or "pickle"
                )
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module == "pickle":
            for alias in node.names:
                if alias.name in {"load", "loads"}:
                    self.pickle_function_aliases.add(
                        alias.asname or alias.name
                    )

        elif node.module == "subprocess":
            for alias in node.names:
                if alias.name in self.SUBPROCESS_FUNCTIONS:
                    self.subprocess_function_aliases.add(
                        alias.asname or alias.name
                    )

        self.generic_visit(node)

    def is_mutable_default(self, node):
        if isinstance(
            node,
            (
                ast.List,
                ast.Dict,
                ast.Set,
                ast.ListComp,
                ast.DictComp,
                ast.SetComp,
            ),
        ):
            return True

        if isinstance(node, (ast.Tuple, ast.Dict)):
            elements = (
                node.elts if isinstance(node, ast.Tuple)
                else [item for pair in node.values for item in pair if item]
            )
            return any(
                self.is_mutable_default(element)
                for element in elements
            )

        if isinstance(node, ast.Call):
            return (
                isinstance(node.func, ast.Name)
                and node.func.id in {"list", "dict", "set"}
            )

        return False

    def visit_function(self, node):
        defaults = list(node.args.defaults)
        defaults.extend(
            default
            for default in node.args.kw_defaults
            if default is not None
        )

        for default in defaults:
            if self.is_mutable_default(default):
                self.add_issue(
                    default,
                    "HIGH",
                    "MUTABLE_DEFAULT",
                    f"Function '{node.name}' uses a mutable default argument.",
                )

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.visit_function(node)

    def visit_AsyncFunctionDef(self, node):
        self.visit_function(node)

    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.add_issue(
                node,
                "MEDIUM",
                "BARE_EXCEPT",
                "Bare except catches unexpected exceptions.",
            )
        self.generic_visit(node)

    def get_call_name(self, func):
        if isinstance(func, ast.Name):
            return func.id

        if isinstance(func, ast.Attribute):
            parent = self.get_call_name(func.value)
            return f"{parent}.{func.attr}" if parent else func.attr

        return ""

    def visit_Call(self, node):
        call_name = self.get_call_name(node.func)

        if isinstance(node.func, ast.Name):
            if node.func.id in {"eval", "exec"}:
                self.add_issue(
                    node,
                    "HIGH",
                    "DYNAMIC_EXECUTION",
                    f"Use of {node.func.id}() may execute unsafe code.",
                )

        # Detect subprocess calls that explicitly enable shell execution.
        parts = call_name.split(".")
        is_subprocess_call = (
            len(parts) == 2
            and parts[0] in self.subprocess_aliases
            and parts[1] in self.SUBPROCESS_FUNCTIONS
        ) or (
            isinstance(node.func, ast.Name)
            and node.func.id in self.subprocess_function_aliases
        )

        if is_subprocess_call:
            for keyword in node.keywords:
                if (
                    keyword.arg == "shell"
                    and isinstance(keyword.value, ast.Constant)
                    and keyword.value.value is True
                ):
                    self.add_issue(
                        node,
                        "HIGH",
                        "SUBPROCESS_SHELL_TRUE",
                        "subprocess call enables shell=True, which can "
                        "create command injection risks.",
                    )
                    break

        # Detect pickle deserialization calls.
        if len(parts) == 2:
            module, function = parts
            if (
                module in self.pickle_aliases
                and function in {"load", "loads"}
            ):
                self.add_issue(
                    node,
                    "HIGH",
                    "UNSAFE_DESERIALIZATION",
                    f"pickle.{function}() can execute code when loading "
                    "untrusted data.",
                )

        elif (
            isinstance(node.func, ast.Name)
            and node.func.id in self.pickle_function_aliases
        ):
            self.add_issue(
                node,
                "HIGH",
                "UNSAFE_DESERIALIZATION",
                f"{node.func.id}() can execute code when loading "
                "untrusted data.",
            )

        self.generic_visit(node)

    def analyze(self, source, filename="<string>"):
        self.issues = []
        self.subprocess_aliases = set()
        self.subprocess_function_aliases = set()
        self.pickle_aliases = set()
        self.pickle_function_aliases = set()

        tree = ast.parse(source, filename=filename)
        self.visit(tree)

        return sorted(
            self.issues,
            key=lambda issue: issue.line,
        )


def review_file(path):
    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    analyzer = ReviewAnalyzer()
    return analyzer.analyze(source, filename=path)


def format_report(issues):
    if not issues:
        return "No review issues found."

    lines = [f"Found {len(issues)} issue(s):"]

    for issue in issues:
        lines.append(
            f"[{issue.severity}] Line {issue.line} "
            f"{issue.rule}: {issue.message}"
        )

    return "\n".join(lines)
