function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total *= prices[i];
    }

    return total;
}

const prices = [10, 20, 30];
const result = calculateTotal(prices);

console.log("Total price:", result);
