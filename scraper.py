import requests
from bs4 import BeautifulSoup, NavigableString



def quotes_by_author(author, page_num=None):

	author = author.replace(" ", "+")

	all_quotes = []

	# if page number not specified, get true page number
	if page_num is None:
		try:
			page = requests.get("https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q="+ author +"&commit=Search")
			soup = BeautifulSoup(page.text, 'html.parser')
			pages = soup.find(class_="smallText").text
			a = pages.find("of ")
			page_num = pages[a+3:]
			page_num = page_num.replace(",", "").replace("\n", "")
			page_num = int(page_num)
			print("looking through", page_num, "pages")
		except:
			page_num = 1

	# for each page
	for i in range(1, page_num+1):

		try:
			page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" + str(i) + "&q=" + author + "&utf8=%E2%9C%93")
			soup = BeautifulSoup(page.text, 'html.parser')
			print("scraping page", i)
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		except:
			print("could not connect to goodreads")
			break
			
		try:
			quote = soup.find(class_="leftContainer")
			quote_list = quote.find_all(class_="quoteDetails")
			# print(quote_list)
			# print("\n\n\n\n\n\n\n\n\n\n\n\n")
		except:
			pass

		# get data for each quote
		for quote in quote_list:

			meta_data = []

			# Get quote's text
			try:
				outer = quote.find(class_="quoteText")
				# print(outer.text)
				# inner_text = [element.strip() for element in outer if isinstance(element, NavigableString)]
				inner_text = [element.strip() for element in outer if isinstance(element, NavigableString)]
				# print(inner_text)
				new_quote = ""
				for i in range(len(inner_text)):
					if '“' in inner_text[i] or '”' in inner_text[i]:
						new_quote += inner_text[i] + " "
				# print(new_quote)
				meta_data.append(new_quote)
			except:
				print("Text is not available")


			# Get quote's author
			try:
				author = quote.find(class_="authorOrTitle").text
				author = author.replace(",", "")
				author = author.replace("\n", "")
				meta_data.append(author.strip())
				# print(author)
			except:
				meta_data.append("PEANUTS")

			# Get quote's book title
			try: 
				title = quote.find(class_="authorOrTitle")
				title = title.nextSibling.nextSibling.text
				title = title.replace("\n", "")
				meta_data.append(title.strip())
				# print(title)
			except:
				meta_data.append(None)

			# Get quote's tags
			try:
				tags = quote.find(class_="greyText smallText left").text
				tags = [x.strip() for x in tags.split(',')]
				tags = tags[1:]
				meta_data.append(tags)
				# print(tags)
			except:
				meta_data.append(None)

			all_quotes.append(meta_data)

		
		# print(all_quotes)
		for text, author, title, tags in all_quotes:
				print("\n\n")
				print(text)
				print(f"- {author}")
				# if title == None:
				# 	pass
				# else:
				# 	print(title)
	
	return all_quotes

quotes_by_author("william burroughs", 1)