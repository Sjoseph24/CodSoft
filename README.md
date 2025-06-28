# CodSoft #2
🎮 Tic-Tac-Toe Game (Python GUI)

This is a simple **Tic-Tac-Toe game** built using **Python and Tkinter**, where the human player (`X`) plays against a computer opponent (`O`) that makes **random moves**.

---

 🧠 Features

- 3x3 **graphical board** with clickable buttons.
- Human player always starts first as **X**.
- Computer plays as **O** and selects moves randomly.
- Game detects:
  - ✅ Win (for either player)
  - 🤝 Draw
- Simple **reset mechanism** after each game.

---

 📦 Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

---

The game window will open.] Click on the boxes to make your move.

📜 Code Overview
board: List storing the state of the 3x3 grid.

on_button_click(i): Handles human player’s move.

computer_move(): Makes a random valid move for the computer.

check_winner(player): Checks all win conditions for a given player.

reset_game(): Resets the board after a win or draw.

buttons: List of all 9 Tkinter buttons on the GUI.

---

🧪 Example Gameplay
Player clicks on a box → it marks 'X'

Computer instantly plays 'O' in a random empty box

Message box shows result (win/draw), then game resets



