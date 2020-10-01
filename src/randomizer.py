from data import Data
from time import time
from random import choice
from langdetect import detect  # type: ignore


class Random:

    path = 'data.json'

    @classmethod
    def getRandom(cls, i=0) -> str:
        """Return random quote as string"""
        i += 1
        all_quotes = Data.load(cls.path)
        random_quote = choice(all_quotes)
        if cls.checkTimestamp(random_quote) is True or i > 80 and detect(random_quote) == "en":
            random_quote["timestamp"] = time()
            Data.save(cls.path, all_quotes)
            return f"\n{random_quote['text']}\n\n - {random_quote['author']}\n"
        else:
            return Random.getRandom(i)

    @staticmethod
    def checkTimestamp(quote):
        """Return bool if quote timestamp is less than 30 days"""
        old_timestamp = quote["timestamp"]
        new_timestamp = time()
        month_seconds = 2592000
        if old_timestamp is None or new_timestamp - old_timestamp > month_seconds:
            return True
        elif new_timestamp - old_timestamp < month_seconds:
            return False
