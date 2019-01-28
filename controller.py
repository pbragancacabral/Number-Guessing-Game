import model
import view

tries = 0
guess = 0


def prompt_for_guess():
    global tries
    global guess
    while True:
        try:
            guess = view.request_guess()
            tries += 1
        except ValueError:
            view.display("That's not a number")
        else:
            return guess


def display_outcome():
    view.display(f"You did it in {tries} tries.")


def start_game():
    model.generate_random_number()
    prompt_for_guess()
    while guess != model.random_number:
        prompt_for_guess()
    display_outcome()


if __name__ == '__main__':
    start_game()
