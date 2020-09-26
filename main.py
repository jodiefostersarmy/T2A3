import data
from randomizer import get_random


options = input("""What would you like to do?
1 - Add author or title
2 - Get me a random quote

Select: """)

if int(options) == 1:
    author_or_title = input("What author or title would you like quotes from? ")
    data.store_quotes(author_or_title) ### test line
elif int(options) == 2:
    print('\n')
    print(get_random())
    print('\n')