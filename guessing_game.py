import os
import random

high_score = None


def display_error(error):
    print(f"Error: {error}")


def display_header():
    print("""===================================
Welcome to the Number Guessing Game
===================================""")


def ask_option():
    print("PLAY - to play the game")
    print("QUIT - to quit the game ")
    print()
    return input("Please select an option: ")


def ask_for_guess():
    guess = int(input("Please select a number between 1 and 10: "))
    if guess < 1 or guess > 10:
        raise ValueError("That number is out of range")
    return guess


def give_hint(user_guess, answer):
    if user_guess != answer:
        if user_guess < answer:
            print("Try higher")
        else:
            print("Try lower")


def guess():
    global high_score
    print("High score (least guesses):",
          "not set" if high_score is None else high_score)
    answer = random.randint(1, 10)
    user_guess = None
    number_of_attempts = 0

    while user_guess != answer:
        try:
            user_guess = ask_for_guess()
            number_of_attempts += 1
            give_hint(user_guess, answer)
        except ValueError as error:
            display_error(error)
            continue

    print("Took you:", number_of_attempts, "attempts")

    if not high_score or high_score > number_of_attempts:
        high_score = number_of_attempts
        print("You have set a new record!")

    again = input("Play again? YES/NO: ")
    clear_screen()
    if again.upper() == "YES":
        guess()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_menu():
    while True:
        try:
            option = ask_option().upper()
            if option == "QUIT":
                clear_screen()
                break
            elif option == "PLAY":
                clear_screen()
                guess()
            else:
                raise ValueError("That's not an option")
        except ValueError as error:
            display_error(error)
        else:
            break


if __name__ == "__main__":
    display_header()
    display_menu()
