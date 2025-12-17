# Rock, Paper, Scissors Game

import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choose one:")
    print("rock")
    print("paper")
    print("scissors")

    user_choice = input("Enter your choice: ").lower()
    options = ["rock", "paper", "scissors"]

    if user_choice not in options:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(options)

    print("User choice:", user_choice)
    print("Computer choice:", computer_choice)

    # Game Logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: You Lose!")
        computer_score += 1

    # Display scores
    print("Score:")
    print("User:", user_score)
    print("Computer:", computer_score)

    # Play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
