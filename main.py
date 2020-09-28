import os
from data import Data
from randomizer import Random

def question():
    options = input("""What would you like to do?

    1 - Add author or title
    2 - Get me a random quote
    3 - Exit

Select: """)

    if int(options) == 1:
        author_or_title = input("What author or title would you like quotes from? ")
        print("Loading quotes into your library...")
        Data.store(author_or_title) ### test line
        print("\nLibrary updated!\n")
        question()
    
    elif int(options) == 2:
        if os.stat("data.json").st_size == 0:
            print("\nYour database is empty, please add an author or title.\n")
            question()
        else:
            print('\n')
            print(Random().getRandom())
            print('\n\n')
            question()
    
    elif int(options)== 3:
        exit()

print("\n\n'Perception is reality' // Lee Atwater\n\n")
question()
