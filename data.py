import json
from scraper import quotes_by_author 


# look to Term 2 Day 16 for ideas on how to refactor into classes and objects

# file scrapes and stores the data from selected authors into the json file
# class Data():

#     @classmethod
#     def save(clas, path, data):
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

def get_quotes(author_or_title):
    
    with open("data.json", "w") as data:
        json_quotes = json.dumps(quotes_by_author(author_or_title, 1))
        data.write(json_quotes)

# get_quotes("william burroughs")

def load_quotes():
    with open("data.json", "r") as data:
        raw_json = data.readline()
        quotes = json.loads(raw_json)
        return quotes
