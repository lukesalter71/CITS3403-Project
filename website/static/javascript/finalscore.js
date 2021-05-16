const username = document.getElementById('username');
const finalScore = document.getElementById('finalScore');
const mostRecentScore = localStorage.getItem('mostRecentScore');

const highScores = JSON.parse(localStorage.getItem('highScores')) || [];

const MAX_HIGH_SCORES = 5;

finalScore.innerText = "Your final score is " + mostRecentScore;
saveHighScore = (e) => {
    e.preventDefault();

    const score = {
        score: mostRecentScore,
    };
    highScores.push(score);
    highScores.sort((a, b) => b.score - a.score);
    highScores.splice(5);

    localStorage.setItem('highScores', JSON.stringify(highScores));
    fetch("/score", {
        method: "POST",
        body: JSON.stringify(score)
    }).then(res => {
        console.log("Request complete! response:", res);
    });
    window.location.assign('/profile');
};