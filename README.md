# Rock, Paper, Scissors Game

This Python program is a simple implementation of the classic "Rock, Paper, Scissors" game. Players can compete against the computer to see who wins based on the traditional rules of the game.

## Features
- User can choose between Rock, Paper, and Scissors.
- Computer randomly selects Rock, Paper, or Scissors.
- The program determines the winner based on the rules of the game.
- Outputs visual representations of the chosen options for a more interactive experience.

---

## Rules of the Game
1. **Rock vs Scissors**: Rock crushes Scissors. Rock wins.
2. **Paper vs Rock**: Paper covers Rock. Paper wins.
3. **Scissors vs Paper**: Scissors cut Paper. Scissors win.
4. If both players choose the same, it's a draw.

---

## How to Run
1. Ensure you have Python installed on your system.
2. Copy the code from the file `rock_paper_scissors.py`.
3. Run the code in your Python IDE or terminal using:
   ```
   python rock_paper_scissors.py
   ```
4. Follow the prompts to select your choice (0 for Rock, 1 for Paper, 2 for Scissors).
5. The program will display both your choice and the computer's choice, along with the result.

---

## Code Overview

### ASCII Art for Choices
The program uses ASCII art to visually represent Rock, Paper, and Scissors:
- **Rock**:
  ```
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  ```
- **Paper**:
  ```
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  ```
- **Scissors**:
  ```
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  ```

### Key Components
- **`IMAGE` List**:
  Stores the names of the options (Rock, Paper, Scissors).

- **User Input**:
  Prompts the user to enter their choice (0 for Rock, 1 for Paper, 2 for Scissors).

- **Random Computer Choice**:
  The computer randomly selects an option using `random.randint(0, 2)`.

- **Game Logic**:
  Determines the winner based on the following:
  - If both choices are the same, it’s a draw.
  - Otherwise, the game checks specific conditions to decide if the user wins or loses.

- **Invalid Input Handling**:
  If the user enters a number outside the range 0–2, the program prints an error message and declares the user as the loser.

---

## Example Output
### Example 1: User Wins
```
What do you choose? Type 0 for rock, 1 for paper, 2 for scissor  1
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

you Win!
```

### Example 2: Draw
```
What do you choose? Type 0 for rock, 1 for paper, 2 for scissor  2
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Its a draw
```

---

## Requirements
- Python 3.x

## Improvements
1. Add a scoring system to keep track of wins, losses, and draws.
2. Allow the user to play multiple rounds in a single session.
3. Enhance input validation to handle non-numeric entries gracefully.
4. Add more visuals or animations for an engaging experience.

---

## License
This project is open-source and free to use. Modify and enhance it as per your requirements!

