async function calculateTotal(prices) {
    const totals = await Promise.all(
        prices.map(async (price) => {
            const tax = await calculateTax(price);
            return price + tax;
        })
    );

    return totals.reduce((sum, value) => sum + value, 0);
}

function calculateTax(price) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(price * 0.1);
        }, 50);
    });
}

async function main() {
    const prices = [100, 200, 300];
    const total = await calculateTotal(prices);
    console.log("Total:", total);
}

main();
