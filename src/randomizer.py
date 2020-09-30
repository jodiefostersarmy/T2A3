from data import Data
from time import time
from random import choice
from langdetect import detect  # type: ignore


class Random:

    path = 'data.json'

    def getRandom(self, i=0) -> str:
        i += 1
        all_quotes = Data.load(self.path)
        random_quote = choice(all_quotes)
        if self.checkTimestamp(random_quote) is True or i > 80 and detect(random_quote) == "en":
            random_quote["timestamp"] = time()
            Data.save(self.path, all_quotes)
            return """
{}

- {}
""".format(random_quote["text"], random_quote["author"])
        else:
            return Random().getRandom(i)

    @staticmethod
    def checkTimestamp(quote):
        old_timestamp = quote["timestamp"]
        new_timestamp = time()
        month_seconds = 2592000
        if old_timestamp is None or new_timestamp - old_timestamp > month_seconds:
            return True
        elif new_timestamp - old_timestamp < month_seconds:
            return False
