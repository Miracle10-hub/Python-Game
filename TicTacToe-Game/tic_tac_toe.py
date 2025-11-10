# 🎮 Tic Tac Toe Game in Python (Beginner Friendly)
# Created by Miracle Nkundabela

from tkinter import *

# Create main window
window = Tk()
window.title("Tic Tac Toe Game")
window.resizable(False, False)

# Start with player X
current_player = "X"

# Create empty 3x3 game board
board = [""] * 9

# Function runs when a player clicks a button
def button_click(i):
    global current_player

    if board[i] == "":
        board[i] = current_player
        buttons[i].config(text=current_player, state="disabled")

        # Check who wins or if it's a tie
        if check_winner(current_player):
            label.config(text=f"🎉 Player {current_player} Wins!")
            disable_all_buttons()
        elif "" not in board:
            label.config(text="😅 It's a tie!")
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s Turn")

# Check all winning combinations
def check_winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Disable all buttons when game ends
def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Restart game
def restart_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    label.config(text="Player X's Turn")
    for btn in buttons:
        btn.config(text="", state="normal")

# Display whose turn it is
label = Label(window, text="Player X's Turn", font=("consolas", 20))
label.grid(row=0, column=0, columnspan=3)

# Create 9 buttons (3x3)
buttons = []
for i in range(9):
    button = Button(window, text="", font=("consolas", 30), width=5, height=2,
                    command=lambda i=i: button_click(i))
    button.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(button)

# Restart button
restart_btn = Button(window, text="Restart", font=("consolas", 18),
                     bg="green", fg="white", command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3, sticky="nsew")

# Run game window
window.mainloop()
