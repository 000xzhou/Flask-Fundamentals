class GuessingGame {
  constructor() {
    this.guessForm = document.getElementById("guess");
    this.listOfWords = document.getElementById("listOfWords");
    this.scoreItem = document.getElementById("score");
    this.bestscoreDoc = document.getElementById("bestscore");
    this.totalGames = document.getElementById("totalGames");
    this.timerItem = document.getElementById("timer");
    this.submitButton = document.getElementById("submit-button");
    this.guessInput = document.getElementById("guess-word");
    this.score = new Set();
    this.timeLeft = 60;

    this.guessForm.addEventListener("submit", this.handleSubmit.bind(this));
    this.startTimer();
  }
  startTimer() {
    this.timerInterval = setInterval(() => {
      if (this.timeLeft > 0) {
        this.timeLeft -= 1;
        this.timerItem.textContent = `Time Left: ${this.timeLeft}s`;
      } else {
        clearInterval(this.timerInterval);
        this.timerExpired();
      }
    }, 1000);
  }
  timerExpired() {
    // Disable the input and submit button, or any other logic you want
    this.guessInput.disabled = true;
    this.submitButton.disabled = true;
    const data = { score: this.score.size };
    const jsonData = JSON.stringify(data);
    fetch("/score", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsonData,
    })
      .then((response) => response.json())
      .then((responseData) => this.handleScoreData(responseData))
      .catch((error) => {
        alert(`Error: ${error}`);
        console.error("Error:", error);
      });
    alert("Time's up!");
  }

  handleSubmit(event) {
    event.preventDefault();

    let input = document.getElementById("guess-word");
    let guessWord = input.value.trim();

    if (guessWord === "") {
      alert("Ensure you input a value!");
      return;
    }

    this.submitGuess(guessWord);
    input.value = "";
  }

  submitGuess(guessWord) {
    const data = { guessWord };
    const jsonData = JSON.stringify(data);

    fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsonData,
    })
      .then((response) => response.json())
      .then((data) => this.handleResponse(data, guessWord))
      .catch((error) => {
        alert(`Error: ${error}`);
        console.error("Error:", error);
      });
  }

  handleResponse(data, guessWord) {
    console.log("Success:", data);
    let li = document.createElement("li");
    li.textContent = `${guessWord}: ${data.result}`;
    if (this.listOfWords.children.length < 10) {
      this.listOfWords.prepend(li); // add to top of list
    } else {
      this.listOfWords.removeChild(this.listOfWords.lastChild);
      this.listOfWords.prepend(li); // add to top of list
    }
    if (data.result === "ok") {
      this.score.add(guessWord);
    }

    this.scoreItem.textContent = this.score.size;
  }
  handleScoreData(responseData) {
    console.log("Success:", responseData);
    this.bestscoreDoc.textContent = responseData.best_score;
    this.totalGames.textContent = responseData.total_games;
  }
  startGame(bestScore, totalGames) {
    this.score = new Set();
    this.timeLeft = 60;
    this.guessInput.disabled = false;
    this.submitButton.disabled = false;
    this.listOfWords.innerHTML = "";
    this.scoreItem.textContent = "0";
    this.timerItem.textContent = `Time Left: 60s`;
    this.totalGames.textContent = totalGames;
    this.bestscoreDoc.textContent = bestScore;
    clearInterval(this.timerInterval);
    this.startTimer();
  }
}
fetch("/start", {
  method: "GET",
  headers: { "Content-Type": "application/json" },
})
  .then((response) => response.json())
  .then((responseData) => {
    let best = responseData.best_score;
    let total = responseData.total_games;
    // Instantiate the class
    const game = new GuessingGame();
    game.startGame(best, total);
  })
  .catch((error) => {
    alert(`Error: ${error}`);
    console.error("Error:", error);
  });

startBtn = document.getElementById("start-button");
startBtn.addEventListener("click", () => {
  window.location.reload();
});
