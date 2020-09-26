from data import load_quotes, save
from time import time
import random
from datetime import date

# create class and create methods for each function below

def select_random(quotes):
    random_choice = random.choice(quotes)
    return random_choice

def test_random(i=0):
    i += 1
    all_quotes = load_quotes()
    random_quote = select_random(all_quotes)
    if check_timestamp(random_quote) is True or i > 150:
        random_quote["timestamp"] = time()
        save(all_quotes)
        return random_quote
    else:
        return test_random(i)

def check_timestamp(quote):
    old_timestamp = quote["timestamp"]
    new_timestamp = time()
    month_seconds = 2592000   
    if old_timestamp == None or new_timestamp - old_timestamp > month_seconds:
        return True
    elif new_timestamp - old_timestamp < month_seconds:
        return False

print(test_random())

# this function will change the timestamp and update the json file with date
# def update_timestamp(quote):
