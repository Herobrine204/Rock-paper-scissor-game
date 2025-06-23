import tkinter as tk
import random

options = ["Rock", "Paper", "Scissors"]


user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(options)
    result_text = ""

    if user_choice == comp_choice:
        result_text = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result_text = "You Win!"
        user_score += 1
    else:
        result_text = "Computer Wins!"
        computer_score += 1

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's Choice: {comp_choice}")
    result_label.config(text=f"Result: {result_text}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    comp_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score - You: 0 | Computer: 0")


window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("400x350")
window.config(bg="#f0f0f0")


title = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

user_choice_label = tk.Label(window, text="Your Choice: ", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()

comp_choice_label = tk.Label(window, text="Computer's Choice: ", font=("Arial", 12), bg="#f0f0f0")
comp_choice_label.pack()

result_label = tk.Label(window, text="Result: ", font=("Arial", 12), fg="blue", bg="#f0f0f0")
result_label.pack(pady=5)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(window, bg="#f0f0f0")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play_game("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play_game("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play_game("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(window, text="Reset", width=10, command=reset_game)
reset_btn.pack(pady=5)

exit_btn = tk.Button(window, text="Exit", width=10, command=window.quit)
exit_btn.pack()


window.mainloop()
