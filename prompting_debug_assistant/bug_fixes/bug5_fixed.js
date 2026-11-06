function sortScores(scores) {
    return [...scores].sort((a, b) => a - b);
}

const scores = [100, 25, 3, 45, 9];
const sortedScores = sortScores(scores);

console.log("Original scores:", scores);
console.log("Sorted scores:", sortedScores);

module.exports = sortScores;
