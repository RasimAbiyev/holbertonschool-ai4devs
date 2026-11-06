function sortScores(scores) {
    return [...scores].sort((a, b) => a - b);
}

function test(input, expected, description) {
    const actual = sortScores(input);
    const passed = JSON.stringify(actual) === JSON.stringify(expected);

    print(
        (passed ? "PASS" : "FAIL") +
        " | " + description +
        " | Expected: " + JSON.stringify(expected) +
        " | Actual: " + JSON.stringify(actual)
    );

    if (!passed) {
        throw new Error("Test failed: " + description);
    }
}

test([100, 25, 3, 45, 9], [3, 9, 25, 45, 100], "Numeric sorting");
test([1, 2, 3], [1, 2, 3], "Already sorted array");
test([], [], "Empty array");

const original = [30, 10, 20];
sortScores(original);

if (JSON.stringify(original) !== "[30,10,20]") {
    throw new Error("Original array was modified");
}

print("PASS | Original array remains unchanged");
