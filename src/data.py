import json
from scraper import Scraper
import os


class Data():

    @classmethod
    def store(cls, userInput):
        """Store scraped data into json file"""
        scan = Scraper.quotes_by_author(userInput, 10)

        if os.stat("data.json").st_size == 0:
            if len(scan) == 0 or scan[0] is None:
                print(f"\nSorry, we couldn't find anything for '{userInput}'\n")
            else:
                with open("data.json", "w") as data:
                    json_quotes = json.dumps(scan)
                    data.write(json_quotes)
                    print("\nLibrary updated!\n")
        else:
            json_decoder = Data.load('data.json')
            if len(scan) > 0:
                for quote in scan:
                    json_decoder.append(quote)
                Data.save('data.json', json_decoder)
                print("\nLibrary updated!\n")
            else:
                print("\nSorry, we did not recognise this author/title\n")

    @classmethod
    def save(cls, path, data):
        """Save into JSON datatype"""
        try:
            with open("data.json", "w") as file_handler:
                json_string = json.dumps(data)
                file_handler.write(json_string)
            return True
        except (KeyboardInterrupt, SystemExit):
            raise "\nSorry, there is nothing to open.\n"

    @classmethod
    def load(cls, path):
        """Convert JSON datatype and return as Python datatype"""
        try:
            with open("data.json", "r") as data:
                raw_json = data.readline()
                quotes = json.loads(raw_json)
                return quotes
        except (KeyboardInterrupt, SystemExit):
            raise "\nSorry, there is nothing to load.\n"
