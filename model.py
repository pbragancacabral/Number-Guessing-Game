import random

random_number = None


def generate_random_number(minimum=1, maximum=10):
    return random.randint(minimum, maximum)


def validate(guess):
    guess = int(guess)
    return guess


def apply_guess(guess):
    guess = validate(guess)
    return guess == random_number
