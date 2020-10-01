import unittest
from time import time
from random import choice
from langdetect import detect  # type: ignore
from data import Data
from randomizer import Random



class TestRandomFunctions(unittest.TestCase):
    

    def test_getRandom(self):
        
        test_data = Data.load('test_data.json')
        self.assertIsInstance(test_data, list)

        random_quote = choice(test_data)
        self.assertIsInstance(random_quote, dict)

        self.assertEqual(Random.getRandom('test_data.json'), '\n“Simplicity, patience, compassion. you reconcile all beings in the world.” \n\n - Lao Tzu\n')

    def test_checkTimestamp(self):
        
        test_data = Data.load('test_data.json')
        random_quote = choice(test_data)
        self.assertEqual(Random.checkTimestamp(random_quote), True)

