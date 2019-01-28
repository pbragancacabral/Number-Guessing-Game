from architecture.entities import random_number

solution = None


def start():
    global solution
    solution = random_number.generate_random_number()


def is_won(guess):
    global solution
    return guess == solution


def hint(guess):
    if guess < solution:
        return "Your guess is too low."
    elif guess > solution:
        return "Your guess is too high."
