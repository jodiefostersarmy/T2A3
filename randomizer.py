from data import load_quotes, save
from time import time
import random
from datetime import date

# create class and create methods for each function below

# this function will select a random quote
def select_random(quotes):
    random_choice = random.choice(quotes)
    return random_choice

quotes = load_quotes() #loads all quotes saved

random_quote = select_random(quotes) # selects a random quote and stores it

print(random_quote["text"])
print(random_quote["author"])

random_quote["timestamp"] = time() # updates timestamp to new time

save(quotes) # saves quotes again into json string

def test_random(selected):


# this function will check the timestamp
def check_timestamp(quote):
    old_timestamp = random_quote["timestamp"]
    new_timestamp = time()
    month_seconds = 2592000
    
    if new_timestamp - old_timestamp > month_seconds:
        return True
    elif new_timestamp - old_timestamp > month_seconds:
        return False


# this function will change the timestamp and update the json file with date
# def update_timestamp(quote):



# def select_random():
#     random_choice = random.choice(load_quotes())
#     random_choice["timestamp"] = date.today()
#     choice_quote = random_choice["text"]
#     choice_author = random_choice["author"]
#     choice_datestamp = random_choice["timestamp"]

#     print("""{} 

# - {}
# {}""".format(choice_quote, choice_author, choice_datestamp))

# select_random()