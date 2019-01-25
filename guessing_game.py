import random


def start_game():
    attempts = 0

    print("Welcome to the number guessing game.")
    random_number = random.randint(1, 1)
    while True:
        attempts += 1

        guess = int(input("What is the number?"))
        if guess > random_number:
            print("It's lower.")
        elif guess < random_number:
            print("It's higher.")
        else:
            print("Got it!")
            break

    print(f"It took you {attempts} attempts.")


if __name__ == '__main__':
    start_game()
