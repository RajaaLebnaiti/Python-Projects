import tkinter as tk
from tkinter import messagebox

squares = [' ']*9
players = ['X', 'O']

win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal axes
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical axes
    (0, 4, 8), (2, 4, 6)               # diagonal axes
]

def check_win(player):
    for a, b, c in win_conditions:
        if {squares[a], squares[b], squares[c]} == {player}:
            return True
    return False

def on_click(index):
    if squares[index] == ' ':
        squares[index] = players[0]
        if check_win(players[0]):
            messagebox.showinfo("Game Over", f"{players[0]} is the winner!")
            reset_game()
        elif ' ' not in squares:
            messagebox.showinfo("Game Over", "No winner!")
            reset_game()
        else:
            players[0], players[1] = players[1], players[0]
            update_board()

def reset_game():
    global squares
    squares = [' ']*9
    update_board()

def update_board():
    for i in range(9):
        buttons[i].config(text=squares[i])

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=' ', font=('Helvetica', 24), width=5, height=2, command=lambda i=i: on_click(i))
    button.grid(row=row, column=col, sticky="nsew")
    buttons.append(button)

reset_button = tk.Button(root, text='Reset', command=reset_game)
reset_button.grid(row=3, column=1, sticky="nsew")

root.mainloop()
