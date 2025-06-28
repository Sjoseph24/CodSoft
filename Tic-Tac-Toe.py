import random
import tkinter as tk
from tkinter import messagebox
import math
root=tk.Tk()
root.title("Tic-Tac-Toe")
board=[' ']*9
buttons=[]
for i in range(9):
    button = tk.Button(root, text=' ', font=('Arial', 24), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

def on_button_click(i):
    if board[i] == ' ':
        board[i] = 'X'
        buttons[i].config(text='X')
        if check_winner('X'):
            messagebox.showinfo("Game Over", "Player X wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            computer_move()

def computer_move():
    empty_indices = [i for i, x in enumerate(board) if x == ' ']
    if empty_indices:
        i = empty_indices[math.floor(random.random() * len(empty_indices))]
        board[i] = 'O'
        buttons[i].config(text='O')
        if check_winner('O'):
            messagebox.showinfo("Game Over", "Player O wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()

def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def reset_game():
    global board
    board = [' ']*9
    for button in buttons:
        button.config(text=' ')

root.mainloop()