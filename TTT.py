# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from string import whitespace

import row
from click import command


def set_title(row, column):
    global game_over, curr_color
    if board[row][column]["text"] != "" or game_over == True:
        return

    global curr_player
    board[row][column]["text"] = curr_player
    if curr_player == playerO:
        curr_player = playerX
        curr_color = col_red
    else:
        curr_player = playerO
        curr_color = col_blue

    board[row][column]["foreground"] = curr_color
    label["text"] = curr_player+"'s turn"
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #hor check
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is a winner!", foreground=col_green)
            for column in range(3):
                board[row][column].config(foreground=col_green, background=col_orange)
            game_over = True
            return

    #ver check
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is a winner!", foreground=col_green)
            for row in range(3):
                board[row][column].config(foreground=col_green, background=col_orange)
            game_over = True
            return

    #diag check
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][column]["text"] != ""):
        label.config(text=board[1][1]["text"] + " is a winner!", foreground=col_green)
        for row in range(3):
            board[row][row].config(foreground=col_green, background=col_orange)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][column]["text"] != ""):
        label.config(text=board[1][1]["text"] + " is a winner!", foreground=col_green)
        for row in range(3):
            board[row][2-row].config(foreground=col_green, background=col_orange)
        game_over = True
        return

    #9 turns check
    if (turns == 9):
        label.config(text="Tie!", foreground=col_green)
        game_over = True
        return

def new_game():
    global turns, game_over, curr_color

    turns = 0
    game_over = False
    label.config(text = curr_player+"'s turn", background="#ffffff",
                 foreground="#343434")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", background="#ffffff", foreground=curr_color)

playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

col_red = "#ff0000"
col_blue = "#0000ff"
col_orange = "#FF4400"
col_green = "#00FF00"
curr_color = col_blue

turns = 0
game_over = False
window = tk.Tk()
window.title("Tic-Tac-Toe v1.0")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=curr_player+"'s turn", font=("Edo SZ", 30), background="#ffffff",
                 foreground="#343434")

label.grid(row=0, column=0, columnspan = 3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Edo SZ", 50, "bold"),
                                       background="#ffffff", foreground=col_blue, width=6, height=2,
                                       command=lambda row=row, column=column: set_title(row,column))
        board[row][column].grid(row=row+1, column= column)

button = tk.Button(frame, text="Restart", font=("Consolas", 30), background=col_orange,
                   foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan = 3, sticky="we")
frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))
#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()
