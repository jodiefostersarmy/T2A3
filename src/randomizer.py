from data import Data
from time import time
from random import choice
from langdetect import detect  # type: ignore


class Random:

    @classmethod
    def getRandom(cls, path: str, i=0) -> str:
        """Return random quote as string"""
        i += 1
        all_quotes = Data.load(path)
        random_quote = choice(all_quotes)
        if cls.checkTimestamp(random_quote) is True or i == len(all_quotes) and detect(random_quote["text"]) == "en":
            random_quote["timestamp"] = time()
            Data.save(path, all_quotes)  # type: ignore
            return f"\n{random_quote['text']}\n\n - {random_quote['author']}\n"
        else:
            return Random.getRandom(path, i)

    @staticmethod
    def checkTimestamp(quote: dict):
        """Return bool if quote timestamp is less than 30 days"""
        old_timestamp = quote["timestamp"]
        new_timestamp = time()
        month_seconds = 2592000
        if old_timestamp is None or new_timestamp - old_timestamp > month_seconds:
            return True
        elif new_timestamp - old_timestamp < month_seconds:
            return False
