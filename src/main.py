import os
from data import Data
from randomizer import Random
from config import Config


def question() -> None:
    """Return user input to call functions and methods with logic"""
    try:
        options: str = input("""What would you like to do?

        1 - Add author or title
        2 - Get me a random quote
        3 - Exit

Select: """)

        if int(options) == 1:
            author_or_title: str = input("\nWhat author or title would you like quotes from? ")
            print("Looking for quotes...")
            print(Data.store(author_or_title))
            question()

        elif int(options) == 2:
            if os.stat(Config.PATH).st_size == 0:
                print("\nYour database is empty, please add an author or title.\n")
                question()
            else:
                print('\n')
                print(Random.getRandom(Config.PATH))
                print('\n\n')
                question()

        elif int(options) == 3:
            print("\nThank you for using Check Your Head!\n")
            exit()

        else:
            print("\nYou must select a number from the options\n")
            question()

    except ValueError:
        print("\nYou must select a number from the options\n")
        question()


print("\n\n'Perception is reality' // Lee Atwater\n\n")
question()
