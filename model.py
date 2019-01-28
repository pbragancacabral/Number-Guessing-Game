import random

random_number = None


def generate_random_number(minimum=1, maximum=2):
    global random_number
    random_number = random.randint(minimum, maximum)
