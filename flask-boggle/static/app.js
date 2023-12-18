class GuessingGame {
  constructor() {
    this.guessForm = document.getElementById("guess");
    this.listOfWords = document.getElementById("listOfWords");
    this.scoreItem = document.getElementById("score");
    this.bestscore = document.getElementById("bestscore");
    this.timerItem = document.getElementById("timer");
    this.submitButton = document.getElementById("submit-button");
    this.guessInput = document.getElementById("guess-word");
    this.score = [];
    this.bestScore = 0;
    // this.timeLeft = 60;
    this.timeLeft = 5;

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

    const data = { score: this.score.length };
    const jsonData = JSON.stringify(data);

    fetch("/score", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsonData,
    })
      .then((response) => response.json())
      .then((responseData) => this.handleScoring(responseData))
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
    this.listOfWords.appendChild(li);

    if (data.result === "ok") {
      this.score.push(guessWord);
    }

    this.scoreItem.textContent = this.score.length;
    console.log(this.score);
  }
  handleScoring(responseData) {
    console.log("Success:", responseData);
    const scoreData = responseData.scoreData;
    const newGameBoard = responseData.newGameBoard;
    handleScoreData(scoreData);
    // updateBoard(newGameBoard);
  }
  handleScoreData(scoreData) {
    if (this.bestScore < scoreData.score) {
      this.bestScore = scoreData.score;
      bestscore.textContent = this.bestScore;
    }
  }
  updateBoard(newGameBoard) {
    console.log(newGameBoard);
    for (let letters in newGameBoard) {
      for (let letter in letters) {
        const letterDoc = document.getElementById("letter");
        letterDoc.textContent = letter;
      }
    }
  }
  startGame() {
    this.score = [];
    // this.timeLeft = 60;
    this.timeLeft = 5;
    this.guessInput.disabled = false;
    this.submitButton.disabled = false;
    this.listOfWords.innerHTML = "";
    this.scoreItem.textContent = "0";
    this.timerItem.textContent = `Time Left: 60s`;
    clearInterval(this.timerInterval);
    this.startTimer();
  }
}

// Instantiate the class
const game = new GuessingGame();
game.startGame();
