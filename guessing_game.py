import random
import sys

answer = random.randint(1, 2)
print("DEBUG:", answer)
high_score = None


def display_header():
    print("Welcome")


def display_menu():
    print("play? ")
    print("quit? ")
    return input("what?")


def play():
    global high_score
    number_of_attempts = 0
    guess = int(input("Guess?"))
    number_of_attempts += 1
    while guess != answer:
        guess = int(input("Guess?"))
        number_of_attempts += 1

    print("Took you:", number_of_attempts, "attempts")

    if not high_score or high_score > number_of_attempts:
        high_score = number_of_attempts
        print("BEATED!")

    again = input("Play again?")
    if again == "yes":
        play()


display_header()
choice = display_menu()
if choice == "quit":
    sys.exit()
elif choice == "play":
    play()
