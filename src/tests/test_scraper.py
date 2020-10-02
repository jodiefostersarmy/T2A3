import unittest
import json
from scraper import Scraper  # type: ignore


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

        quoteList = []
        self.assertIsInstance(Scraper.format_quotes(quoteList), list)

    def test_get_quote_text(self):
        pass

    def test_get_text_title(self):
        pass

    def test_get_text_tags(self):
        pass
