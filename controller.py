import model
import view


def request_guess():
    while True:
        try:
            guess = int(view.ask_for_guess())
        except ValueError as message:
            view.display_error(message)
        else:
            break


def start_game():
    random_number = model.random_number()
    # attempts = 0
    #
    # print("Welcome to the number guessing game.")
    # random_number = random.randint(1, 1)
    # while True:
    #     attempts += 1
    #
    #     guess = int(input("What is the number?"))
    #     if guess > random_number:
    #         print("It's lower.")
    #     elif guess < random_number:
    #         print("It's higher.")
    #     else:
    #         print("Got it!")
    #         break
    #
    # print(f"It took you {attempts} attempts.")
    request_guess()


if __name__ == '__main__':
    start_game()
