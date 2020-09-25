import json
from scraper import quotes_by_author 
import random
from datetime import date

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

with open("data.json", "r") as data:
    raw_json = data.readline()
    quotes = json.loads(raw_json)



random_choice = random.choice(quotes)
random_choice["timestamp"] = date.today()
choice_quote = random_choice["text"]
choice_author = random_choice["author"]
choice_datestamp = random_choice["timestamp"]

print("""{} 

- {}
{}""".format(choice_quote, choice_author, choice_datestamp))

