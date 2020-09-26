from data import load_quotes
import random
from datetime import date

random_choice = random.choice(load_quotes())
random_choice["timestamp"] = date.today()
choice_quote = random_choice["text"]
choice_author = random_choice["author"]
choice_datestamp = random_choice["timestamp"]

print("""{} 

- {}
{}""".format(choice_quote, choice_author, choice_datestamp))
