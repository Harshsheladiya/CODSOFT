import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def normalize_choice(choice):
    choices = {
        'rock': ['rock', 'roke', 'r'],
        'paper': ['paper', 'peper', 'p'],
        'scissors': ['scissors', 'seriser', 's']
    }
    for key, values in choices.items():
        if choice in values:
            return key
    return None

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game:")
        user_input = input("Enter your choice (rock, paper, scissors):-> ").lower()
        user_choice = normalize_choice(user_input)
        
        if user_choice is None:
            print("Invalid choice. Sorry, please correct and try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        choice = input("Play again? (yes/no):-> ")
        if choice.lower() not in ['yes', 'y']:
            break

    print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
