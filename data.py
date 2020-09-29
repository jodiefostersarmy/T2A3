import json
from scraper import quotes_by_author
import os


class Data():
    @classmethod
    def store(cls, user_input):
        if os.stat("data.json").st_size == 0:
            scan = quotes_by_author(user_input, 10)
            if len(scan) == 0:
                print("""
Sorry, we couldn't find anything under this author/title.
""")
            else:
                with open("data.json", "w") as data:
                    json_quotes = json.dumps(quotes_by_author(user_input, 10))
                    data.write(json_quotes)
                    print("\nLibrary updated!\n")
        else:
            json_decoder = Data.load('data.json')
            new_quotes = quotes_by_author(user_input, 10)
            if len(new_quotes) > 0:
                for quote in new_quotes:
                    json_decoder.append(quote)
            else:
                print("\nSorry, we did not recognise this author/title\n")
            Data.save('data.json', json_decoder)

    @classmethod
    def save(cls, path, data):
        try:
            with open("data.json", "w") as file_handler:
                json_string = json.dumps(data)
                file_handler.write(json_string)
                print("\nLibrary updated!\n")
            return True
        except (KeyboardInterrupt, SystemExit):
            raise "\nSorry, there is nothing to open.\n"

    @classmethod
    def load(cls, path):
        try:
            with open("data.json", "r") as data:
                raw_json = data.readline()
                quotes = json.loads(raw_json)
                return quotes
        except (KeyboardInterrupt, SystemExit):
            raise "\nSorry, there is nothing to load.\n"
