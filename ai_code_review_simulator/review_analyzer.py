import ast
from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewIssue:
    line: int
    severity: str
    rule: str
    message: str


class ReviewAnalyzer(ast.NodeVisitor):
    """Detect common Python code review issues using the AST."""

    def __init__(self):
        self.issues = []

    def add_issue(self, node, severity, rule, message):
        self.issues.append(
            ReviewIssue(
                line=node.lineno,
                severity=severity,
                rule=rule,
                message=message,
            )
        )

    def visit_FunctionDef(self, node):
        defaults = node.args.defaults
        for default in defaults:
            if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                self.add_issue(
                    node,
                    "HIGH",
                    "MUTABLE_DEFAULT",
                    f"Function '{node.name}' uses a mutable default argument.",
                )
            elif isinstance(default, ast.Call):
                if isinstance(default.func, ast.Name):
                    if default.func.id in {"list", "dict", "set"}:
                        self.add_issue(
                            node,
                            "HIGH",
                            "MUTABLE_DEFAULT",
                            f"Function '{node.name}' creates a mutable default.",
                        )
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.add_issue(
                node,
                "MEDIUM",
                "BARE_EXCEPT",
                "Bare except catches unexpected exceptions.",
            )
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in {"eval", "exec"}:
                self.add_issue(
                    node,
                    "HIGH",
                    "DYNAMIC_EXECUTION",
                    f"Use of {node.func.id}() may execute unsafe code.",
                )
        self.generic_visit(node)

    def analyze(self, source, filename="<string>"):
        self.issues = []
        tree = ast.parse(source, filename=filename)
        self.visit(tree)
        return sorted(self.issues, key=lambda issue: issue.line)


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
