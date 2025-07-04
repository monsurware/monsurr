import tkinter as tk
import random

# Create main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("300x300")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Result label
result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Game logic
def play(user_choice):
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! Computer chose {computer_choice}"
    else:
        result = f"You Lose! Computer chose {computer_choice}"
    
    result_label.config(text=result)

# Buttons
tk.Button(window, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(window, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

# Run the GUI
window.mainloop()
