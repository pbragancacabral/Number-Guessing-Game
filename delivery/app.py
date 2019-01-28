from architecture.interactors import game
from delivery.view import terminal

game.start()


def ask():
    while True:
        try:
            guess = int(input("Guess?"))
        except ValueError as error:
            print(f"Error: {error}")
        else:
            return guess


guess = None
while not game.is_won(guess):
    guess = ask()
    if game.is_won(guess):
        break
    else:
        terminal.display(game.hint(guess))
