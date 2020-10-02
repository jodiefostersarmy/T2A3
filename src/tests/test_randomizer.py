import unittest
from unittest.mock import patch
from random import choice
from src.randomizer import Random
from src.data import Data


class TestRandomFunctions(unittest.TestCase):

    @patch("randomizer.Data.save")
    def test_getRandom(self, patched):

        test_data = Data.load('test_data.json')
        random_quote = choice(test_data)
        self.assertIsInstance(random_quote, dict)

        self.assertEqual(
            Random.getRandom('test_data.json'),
            '\n“Simplicity, patience, compassion. you reconcile all beings in the world.” \n\n - Lao Tzu\n'
            )

    def test_checkTimestamp(self):
        test_data = Data.load('test_data.json')
        random_quote = choice(test_data)
        self.assertEqual(Random.checkTimestamp(random_quote), True)
