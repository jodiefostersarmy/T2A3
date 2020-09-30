import unittest
from time import time
from random import choice
from langdetect import detect  # type: ignore
from data import Data
from randomizer import Random


class TestRandomFunctions(unittest.TestCase):
    def test_getRandom(self):
        all_quotes = [{"text": "\u201cSimplicity, patience, compassion. you reconcile all beings in the world.\u201d ", "author": "Lao Tzu", "title": "Tao Te Ching", "tags": ["life", "philosophy"], "timestamp": None}]
        self.assertIsInstance(all_quotes, list)

        random_quote = choice(all_quotes)
        self.assertIsInstance(random_quote, dict)

