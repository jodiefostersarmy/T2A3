import json
from scraper import quotes_by_author 
import os

# look to Term 2 Day 16 for ideas on how to refactor into classes and objects

# file scrapes and stores the data from selected authors into the json file
# class Data():

#     @classmethod
#     def save(cls, path, data):
#         @classmethod
#         with open("data.json", "w") as file_handler:
#             json_quotes = json.dumps(quotes_by_author(author_or_title, 1))
#             file_handler.write(json_quotes)

#     @classmethod
#     def load(cls, path):
#         try:
#             with open(path, "r") as file_handler:
#                 json_string - file_handler.read()
#                 return json.loads(json_string)

############################# IGNORE CODE ABOVE THIS LINE FOR NOW ######################

# function below will store all quotes from author/title chosen by user

def store_quotes(user_input):
    if os.stat("data.json").st_size == 0:
        with open("data.json", "w") as data:
            json_quotes = json.dumps(quotes_by_author(user_input, 5))
            data.write(json_quotes)
    else:
        json_decoder = load_quotes()
        new_quotes = quotes_by_author(user_input, 5)
        if len(new_quotes) > 0:
            for quote in new_quotes:
                json_decoder.append(quote)
        else:
            print("Sorry, we did not recognise this author/title")
        save(json_decoder)

def load_quotes():
    with open("data.json", "r") as data:
        raw_json = data.readline()
        quotes = json.loads(raw_json)
        return quotes

def save(data):
    try:
        with open("data.json", "w") as file_handler:
            json_string = json.dumps(data)
            file_handler.write(json_string)
        return True
    except:
        return False