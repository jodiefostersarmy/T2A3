import unittest
import json
from data import Data
from scraper import Scraper

class TestScraperFunctions(unittest.TestCase):

    def test_quotes_by_author(self):

        author = "William Burroughs"
        pageNumber = 1
        self.assertIsInstance(Scraper.quotes_by_author(author, pageNumber), list)

    def test_get_request(self):

        author = "William Burroughs"
        pageNumber = 1
        self.assertIsInstance(Scraper.get_request(author, pageNumber), list)

    def test_format_quotes(self):

        test_data = Data.load('test_data.json')
        

    # def test_save(self):

    #     path = 'test_save.json'
    #     data = [1, 2, 3]
    #     result = Data.save(path, data)
    #     self.assertTrue(result)

    #     with open(path, "r") as file_handler:
    #         contents = file_handler.readline()
    #     self.assertEqual(contents, json.dumps(data))

        # os.remove(path)