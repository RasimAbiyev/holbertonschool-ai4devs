function sortScores(scores) {
    const sortedScores = scores.sort();
    return sortedScores;
}

function displayScores(scores) {
    console.log("Original scores:", scores);

    const result = sortScores(scores);

    console.log("Sorted scores:", result);
}

const scores = [5, 20, 100, 3, 45];

displayScores(scores);
