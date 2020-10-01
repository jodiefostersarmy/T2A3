import unittest
import json
import os
from data import Data


class TestDataFunctions(unittest.TestCase):
    def test_store(self):

        userInput = "Tao Te Ching"
        self.assertEqual(Data.store(userInput), "\nLibrary updated!\n")

    def test_save(self):

        path = 'test_save.json'
        data = [1, 2, 3]
        result = Data.save(path, data)
        self.assertTrue(result)

        with open(path, "r") as file_handler:
            contents = file_handler.readline()
        self.assertEqual(contents, json.dumps(data))

        os.remove(path)
