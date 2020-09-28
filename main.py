import os
from data import Data
from randomizer import Random

def question():
    try:
        options = input("""What would you like to do?

        1 - Add author or title
        2 - Get me a random quote
        3 - Exit

Select: """)

        if int(options) == 1:
            author_or_title = input("What author or title would you like quotes from? ")
            print("Looking for quotes...")
            Data.store(author_or_title) ### test line
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
        
        else:
            print("\nYou must select a number from the options\n")
            question()
            
    except ValueError:
        print("\nYou must select a number from the options\n")
        question()


    

print("\n\n'Perception is reality' // Lee Atwater\n\n")
question()
