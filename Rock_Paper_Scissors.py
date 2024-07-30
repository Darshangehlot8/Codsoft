import random

def play_rock_paper_scissors():
    """Plays a game of Rock,Paper,Scissors against the computer."""

    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)

    user_choice = input("Enter your choice(rock,paper,scissors): ").lower()
    while user_choice not in options:
        print("Invalid choice.Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice(rock,paper,scissors):").lower()

        print(f"You choose: {user_choice}")
        print(f"Computer choose: {computer_choice}")

    if user_choice == computer_choice:
            print("It's a tie!")
    elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
            else:
                print("Computer wins!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
        play_rock_paper_scissors()