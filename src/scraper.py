import requests
import bs4  # type: ignore
from typing import Optional, Union, List, Any, Dict


class Scraper:

    website = "https://www.goodreads.com/quotes/search?commit=Search&page="

    @classmethod
    def quotes_by_author(cls, author: str, pageNumber: int) -> Union[list, str]:
        author = author.replace(" ", "+")
        all_quotes = Scraper.get_request(author, pageNumber)
        return all_quotes

    @staticmethod
    def get_request(author: str, pageNumber: int) -> Union[list, str]:
        """Execute GET request and parse HTML through BeautifulSoup"""
        for i in range(1, pageNumber+1):
            try:
                page = requests.get(Scraper.website + str(i) + "&q=" + author + "&utf8=%E2%9C%93")
                soup = bs4.BeautifulSoup(page.text, 'html.parser')

                quote = soup.find(class_="leftContainer")
                quote_list = quote.find_all(class_="quoteDetails")

                formatted = Scraper.format_quotes(quote_list)

                return formatted
                
            except (ConnectionError, TimeoutError):
                return "\nCould not connect to goodreads\n"

    @staticmethod
    def format_quotes(quoteList: bs4.element.Tag) -> list:
        """Assign returned scrape data into dictionary with static methods"""
        all_meta_data = []

        for quote in quoteList:	 # get data for each quote
            meta_data = {
                "text": None,
                "author": None,
                "title": None,
                "tags": [],
                "timestamp": None
                }  # type: dict
            meta_data["text"] = Scraper.get_quote_text(quote)
            meta_data["author"] = Scraper.get_text_author(quote)
            meta_data["title"] = Scraper.get_text_title(quote)
            meta_data["tags"] = Scraper.get_text_tags(quote)

            all_meta_data.append(meta_data)

        return all_meta_data

    @staticmethod
    def get_quote_text(quote: bs4.element.Tag) -> Optional[str]:
        """Return quote from html tag class as string"""
        try:
            outer = quote.find(class_="quoteText")
            inner_text = [element.strip() for element in outer if isinstance(element, bs4.NavigableString)]
            new_quote = ""
            for i in range(len(inner_text)):
                if '“' in inner_text[i] or '”' in inner_text[i]:
                    new_quote += inner_text[i] + " "
            return new_quote
        except AttributeError:
            return None

    @staticmethod
    def get_text_author(quote: bs4.element.Tag) -> Optional[str]:
        """Return author from html tag class as string"""
        try:
            author = quote.find(class_="authorOrTitle").text
            author = author.replace(",", "")
            author = author.replace("\n", "")
            return author.strip()
        except AttributeError:
            return None

    @staticmethod
    def get_text_title(quote: bs4.element.Tag) -> Optional[str]:
        """Return title from html tag class as string"""
        try:
            title = quote.find(class_="authorOrTitle")
            title = title.nextSibling.nextSibling.text
            title = title.replace("\n", "")
            return title.strip()
        except AttributeError:
            return None

    @staticmethod
    def get_text_tags(quote: bs4.element.Tag) -> Optional[list]:
        """Return tags from html tag class as string"""
        try:
            tags = quote.find(class_="greyText smallText left").text
            tags = [x.strip() for x in tags.split(',')]
            tags = tags[1:]
            return tags.strip()
        except AttributeError:
            return None
