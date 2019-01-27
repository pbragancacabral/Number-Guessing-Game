import model


def ask_for_guess():
    while True:
        try:
            guess = input("Guess? ")
            model.apply_guess(guess)
        except ValueError:
            print("Not a number")
        else:
            break
