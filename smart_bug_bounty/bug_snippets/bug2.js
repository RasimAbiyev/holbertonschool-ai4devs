function calculateTotal(prices) {
    let total = 0;

    prices.forEach(async (price) => {
        const tax = await calculateTax(price);
        total += price + tax;
    });

    return total;
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
