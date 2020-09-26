import json
from scraper import quotes_by_author 


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

def store_quotes(author_or_title):
    with open("data.json", "w") as data:
        json_quotes = json.dumps(quotes_by_author(author_or_title, 1))
        data.write(json_quotes)


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