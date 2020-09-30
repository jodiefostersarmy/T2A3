import json
from scraper import Scraper
import os


class Data():

    @classmethod
    def store(cls, userInput):
        
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
            else:
                print("\nSorry, we did not recognise this author/title\n")

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

    # @staticmethod
    # def create_database(jsonString, userInput):
    #     if os.stat("data.json").st_size == 0:
    #         if len(jsonString) == 0 or jsonString[0] is None:
    #             print(f"\nSorry, we couldn't find anything for '{userInput}'\n")
    #         else:
    #             with open("data.json", "w") as data:
    #                 json_quotes = json.dumps(jsonString)
    #                 data.write(json_quotes)
    #                 print("\nLibrary updated!\n")
    #     else:
    #         json_decoder = Data.load('data.json')
    #         if len(jsonString) > 0:
    #             for quote in jsonString:
    #                 json_decoder.append(quote)
    #             Data.save('data.json', json_decoder)
    #         else:
    #             print("\nSorry, we did not recognise this author/title\n")
