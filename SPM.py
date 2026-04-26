import random

def play_stone_paper_scissors():
    """Stone-Paper-Scissors game"""
    choices = ["Stone", "Paper", "Scissors"]

    print("\n=== Stone, Paper, Scissors ===")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")

    try:
        user_choice = int(input("Enter your choice (1-3): "))
        if user_choice < 1 or user_choice > 3:
            print("Invalid choice! Please enter 1, 2, or 3.")
            return

        user_move = choices[user_choice - 1]
        computer_move = random.choice(choices)

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        if user_move == computer_move:
            print("Result: It's a Tie!")
        elif (user_move == "Stone" and computer_move == "Scissors") or \
             (user_move == "Paper" and computer_move == "Stone") or \
             (user_move == "Scissors" and computer_move == "Paper"):
            print("Result: You Win!")
        else:
            print("Result: Computer Wins!")

    except ValueError:
        print("Invalid input! Please enter a number.")


def play_dice_roll():
    """Dice Roll game"""
    print("\n=== Dice Roll Game ===")
    print("You and the computer each roll a dice (1-6).")
    print("The highest roll wins!")

    try:
        input("Press Enter to roll the dice...")

        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print(f"\nYou rolled: {user_roll}")
        print(f"Computer rolled: {computer_roll}")

        if user_roll > computer_roll:
            print("Result: You Win!")
        elif user_roll < computer_roll:
            print("Result: Computer Wins!")
        else:
            print("Result: It's a Tie!")

    except KeyboardInterrupt:
        print("\nGame cancelled.")


def display_menu():
    """Display main menu"""
    print("\n=== GAME MENU ===")
    print("1. Stone - Paper - Scissors")
    print("2. Dice Roll Game")
    print("3. Exit")
    print("================")


def main():
    """Main game loop"""
    print("Welcome to the Simple Game!")

    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                play_stone_paper_scissors()
            elif choice == "2":
                play_dice_roll()
            elif choice == "3":
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

        except KeyboardInterrupt:
            print("\n\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
