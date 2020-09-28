import requests
import json
from bs4 import BeautifulSoup, NavigableString


### Fix code so that it will scrape all pages for your data needed

def quotes_by_author(author, page_num=None):

	author = author.replace(" ", "+")

	all_quotes = []

	# if page number not specified, get true page number
	# if page_num is None:
	# 	try:
	# 		page = requests.get("https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q="+ author +"&commit=Search")
	# 		soup = BeautifulSoup(page.text, 'html.parser')
	# 		pages = soup.find(class_="smallText").text
	# 		a = pages.find("of ")
	# 		page_num = pages[a+3:]
	# 		page_num = page_num.replace(",", "").replace("\n", "")
	# 		page_num = int(page_num)
	# 	except:
	# 		page_num = 1

	# for each page
	for i in range(1, page_num+1):

		try:
			page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" + str(i) + "&q=" + author + "&utf8=%E2%9C%93")
			soup = BeautifulSoup(page.text, 'html.parser')
		except:
			print("could not connect to goodreads")
			break
			
		try:
			quote = soup.find(class_="leftContainer")
			quote_list = quote.find_all(class_="quoteDetails")
		except:
			pass
		
		#quote OOP turn metadata into a class itself or method
		# get data for each quote
		for quote in quote_list:

			meta_data = {"text": None, "author": None, "title": None, "tags": [], "timestamp": None}

			# Get quote's text
			try:
				outer = quote.find(class_="quoteText")
				# print(outer.text)
				inner_text = [element.strip() for element in outer if isinstance(element, NavigableString)]
				# print(inner_text)
				new_quote = ""
				for i in range(len(inner_text)):
					if '“' in inner_text[i] or '”' in inner_text[i]:
						new_quote += inner_text[i] + " "
				# print(new_quote)
				meta_data["text"] = new_quote
			except:
				pass

			# Get quote's author
			try:
				author = quote.find(class_="authorOrTitle").text
				author = author.replace(",", "")
				author = author.replace("\n", "")
				meta_data["author"] = author.strip()
				# print(author)
			except:
				pass

			# Get quote's book title
			try: 
				title = quote.find(class_="authorOrTitle")
				title = title.nextSibling.nextSibling.text
				title = title.replace("\n", "")
				meta_data["title"] =  title.strip()
				# print(title)
			except:
				pass

			# Get quote's tags
			try:
				tags = quote.find(class_="greyText smallText left").text
				tags = [x.strip() for x in tags.split(',')]
				tags = tags[1:]
				meta_data["tags"] = tags
				# print(tags)
			except:
				pass

			all_quotes.append(meta_data)
	

	return all_quotes



# quotes_by_author("william burroughs", 1)
