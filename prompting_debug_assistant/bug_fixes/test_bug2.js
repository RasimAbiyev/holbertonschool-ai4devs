function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total += prices[i];
    }

    return total;
}

function test(input, expected, description) {
    const actual = calculateTotal(input);
    const passed = actual === expected;

    print(
        (passed ? "PASS" : "FAIL") +
        " | " + description +
        " | Expected: " + expected +
        " | Actual: " + actual
    );

    if (!passed) {
        throw new Error("Test failed: " + description);
    }
}

test([10, 20, 30], 60, "Multiple prices");
test([5], 5, "Single price");
test([], 0, "Empty array");
