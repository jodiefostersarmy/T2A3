from data import Data
from time import time
from random import choice
from datetime import date

class Random:

    path = 'data.json'

    def getRandom(self, i=0):
        i += 1
        all_quotes = Data.load(self.path)
        random_quote = choice(all_quotes)
        if self.checkTimestamp(random_quote) is True or i > 80:
            random_quote["timestamp"] = time()
            Data.save(self.path, all_quotes)
            return """
{} 

- {}
""".format(random_quote["text"], random_quote["author"])
        else:
            return Random().getRandom(i) # why must I put a parenthesis after Random class? Why cant I just use the Random.getRandom()?
    
    @classmethod
    def checkTimestamp(cls, quote):
        old_timestamp = quote["timestamp"]
        new_timestamp = time()
        month_seconds = 2592000   
        if old_timestamp == None or new_timestamp - old_timestamp > month_seconds:
            return True
        elif new_timestamp - old_timestamp < month_seconds:
            return False

random = Random()


print(random.getRandom())







#####DATA BACKUP BELOW####

############################# IGNORE CODE ABOVE THIS LINE FOR NOW ######################

# function below will store all quotes from author/title chosen by user

# def store_quotes(user_input):
#     if os.stat("data.json").st_size == 0:
#         with open("data.json", "w") as data:
#             json_quotes = json.dumps(quotes_by_author(user_input, 10))
#             data.write(json_quotes)
#     else:
#         json_decoder = load_quotes()
#         new_quotes = quotes_by_author(user_input, 10)
#         if len(new_quotes) > 0:
#             for quote in new_quotes:
#                 json_decoder.append(quote)
#         else:
#             print("Sorry, we did not recognise this author/title")
#         save(json_decoder)

# def load_quotes():
#     with open("data.json", "r") as data:
#         raw_json = data.readline()
#         quotes = json.loads(raw_json)
#         return quotes

# def save(data):
#     try:
#         with open("data.json", "w") as file_handler:
#             json_string = json.dumps(data)
#             file_handler.write(json_string)
#         return True
#     except:
#         return False




###### BACKUP CLASS RANDOMIZER TEST ##### 28/09/20

# from data import Data
# from time import time
# import random
# from datetime import date

# path = "data.json"

# def select_random(quotes):
#     random_choice = random.choice(quotes)
#     return random_choice

# def get_random(i=0):
#     i += 1
#     all_quotes = Data.load(path)
#     random_quote = select_random(all_quotes)
#     if check_timestamp(random_quote) is True or i > 150:
#         random_quote["timestamp"] = time()
#         Data.save(path, all_quotes)
#         return """{} 

# - {}""".format(random_quote["text"], random_quote["author"])
#     else:
#         return get_random(i)

# def check_timestamp(quote):
#     old_timestamp = quote["timestamp"]
#     new_timestamp = time()
#     month_seconds = 2592000   
#     if old_timestamp == None or new_timestamp - old_timestamp > month_seconds:
#         return True
#     elif new_timestamp - old_timestamp < month_seconds:
#         return False


