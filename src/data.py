import json
from scraper import Scraper
import os
from typing import Union, Any, List
from config import Config


class Data():

    @classmethod
    def store(cls, userInput: str) -> str:
        """Store scraped data into json file"""
        scan: List[Any] = Scraper.quotes_by_author(userInput, 10)  # type: ignore

        if os.stat(Config.PATH).st_size == 0:
            if len(scan) == 0 or scan[0] is None:
                return f"\nSorry, we couldn't find anything for '{userInput}'\n"
            else:
                with open(Config.PATH, "w") as data:
                    json_quotes = json.dumps(scan)
                    data.write(json_quotes)
                    return "\nLibrary updated!\n"
        else:
            json_decoder: Union[List[dict], str] = Data.load(Config.PATH)
            if len(scan) > 0:
                for quote in scan:
                    json_decoder.append(quote)  # type: ignore
                Data.save(Config.PATH, json_decoder)  # type: ignore
                return "\nLibrary updated!\n"
            else:
                return "\nSorry, we did not recognise this author/title\n"

    @classmethod
    def save(cls, path: str, data: str) -> Union[bool, str]:
        """Save into JSON datatype"""
        try:
            with open(path, "w") as file_handler:
                json_string = json.dumps(data)
                file_handler.write(json_string)
            return True
        except (KeyboardInterrupt, SystemExit):
            return "\nSorry, there is nothing to open.\n"

    @classmethod
    def load(cls, path: str) -> Union[list, str]:
        """Convert JSON datatype and return as Python datatype"""
        try:
            with open(path, "r") as data:
                raw_json = data.readline()
                quotes = json.loads(raw_json)
                return quotes
        except (KeyboardInterrupt, SystemExit):
            return "\nSorry, there is nothing to load.\n"
