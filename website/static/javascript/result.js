const highScoresList = document.getElementById("highScoresList");
const result = JSON.parse(localStorage.getItem("highScores")) || [];

highScoresList.innerHTML = result
  .map(score => {
    return `<li class="high-score">${score.name} - ${score.score}</li>`;
  })
  .join("");