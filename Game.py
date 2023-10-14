
import random

def display_menu():
    print("Menu:")
    print("1. Start game")
    print("2. View rules")
    print("3. Exit")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nChoose: (1) Stone, (2) Paper, (3) Scissors, or (q) Quit: ").lower()
        
        if user_choice == 'q':
            break

        if user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please choose 1, 2, 3, or q.")
            continue

        computer_choice = str(random.randint(1, 3))

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == '1' and computer_choice == '3') or \
             (user_choice == '2' and computer_choice == '1') or \
             (user_choice == '3' and computer_choice == '2'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

def view_rules():
    print("Rules:")
    print("Stone beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Stone")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        play_game()
    elif choice == '2':
        view_rules()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
