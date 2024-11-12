function playRockPaperScissors(playerChoice) {
    const validChoices = ['rock', 'paper', 'scissors'];
    if (!validChoices.includes(playerChoice)) {
        throw new Error("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.");
    }
    const computerRandomNumber = Math.random();
    let computerChoice;
    if (computerRandomNumber < 0.34) {
        computerChoice = 'rock';
    } else if (computerRandomNumber < 0.67) {
        computerChoice = 'paper';
    } else {
        computerChoice = 'scissors';
    }
    console.log(`Player choice: ${playerChoice}`);
    console.log(`Computer choice: ${computerChoice}`);
    if (playerChoice === computerChoice) {
        return "It's a draw!";
    } 
    if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        return "Player wins!";
    } else {
        return "Computer wins!";
    }
}