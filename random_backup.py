from data import Data
from time import time
from random import choice
from datetime import date

class Random:

    path = 'data.json'

    def getRandom(self, i=0):
        i += 1
        all_quotes = Data.load(self.path)
        random_quote = choice(all_quotes)
        if self.checkTimestamp(random_quote) is True or i > 80:
            random_quote["timestamp"] = time()
            Data.save(self.path, all_quotes)
            return """
{} 

- {}
""".format(random_quote["text"], random_quote["author"])
        else:
            return Random().getRandom(i) # why must I put a parenthesis after Random class? Why cant I just use the Random.getRandom()?
    
    @classmethod
    def checkTimestamp(cls, quote):
        old_timestamp = quote["timestamp"]
        new_timestamp = time()
        month_seconds = 2592000   
        if old_timestamp == None or new_timestamp - old_timestamp > month_seconds:
            return True
        elif new_timestamp - old_timestamp < month_seconds:
            return False

random = Random()


print(random.getRandom())







#####DATA BACKUP BELOW####

############################# IGNORE CODE ABOVE THIS LINE FOR NOW ######################

# function below will store all quotes from author/title chosen by user

# def store_quotes(user_input):
#     if os.stat("data.json").st_size == 0:
#         with open("data.json", "w") as data:
#             json_quotes = json.dumps(quotes_by_author(user_input, 10))
#             data.write(json_quotes)
#     else:
#         json_decoder = load_quotes()
#         new_quotes = quotes_by_author(user_input, 10)
#         if len(new_quotes) > 0:
#             for quote in new_quotes:
#                 json_decoder.append(quote)
#         else:
#             print("Sorry, we did not recognise this author/title")
#         save(json_decoder)

# def load_quotes():
#     with open("data.json", "r") as data:
#         raw_json = data.readline()
#         quotes = json.loads(raw_json)
#         return quotes

# def save(data):
#     try:
#         with open("data.json", "w") as file_handler:
#             json_string = json.dumps(data)
#             file_handler.write(json_string)
#         return True
#     except:
#         return False




###### BACKUP CLASS RANDOMIZER TEST ##### 28/09/20

# from data import Data
# from time import time
# import random
# from datetime import date

# path = "data.json"

# def select_random(quotes):
#     random_choice = random.choice(quotes)
#     return random_choice

# def get_random(i=0):
#     i += 1
#     all_quotes = Data.load(path)
#     random_quote = select_random(all_quotes)
#     if check_timestamp(random_quote) is True or i > 150:
#         random_quote["timestamp"] = time()
#         Data.save(path, all_quotes)
#         return """{} 

# - {}""".format(random_quote["text"], random_quote["author"])
#     else:
#         return get_random(i)

# def check_timestamp(quote):
#     old_timestamp = quote["timestamp"]
#     new_timestamp = time()
#     month_seconds = 2592000   
#     if old_timestamp == None or new_timestamp - old_timestamp > month_seconds:
#         return True
#     elif new_timestamp - old_timestamp < month_seconds:
#         return False


### scraper OG #### 28/09/20

# import requests
# import json
# from bs4 import BeautifulSoup, NavigableString


# ### Fix code so that it will scrape all pages for your data needed

# def quotes_by_author(author, page_num=None):

# 	author = author.replace(" ", "+")

# 	all_quotes = []

# 	# if page number not specified, get true page number
# 	# if page_num is None:
# 	# 	try:
# 	# 		page = requests.get("https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q="+ author +"&commit=Search")
# 	# 		soup = BeautifulSoup(page.text, 'html.parser')
# 	# 		pages = soup.find(class_="smallText").text
# 	# 		a = pages.find("of ")
# 	# 		page_num = pages[a+3:]
# 	# 		page_num = page_num.replace(",", "").replace("\n", "")
# 	# 		page_num = int(page_num)
# 	# 	except:
# 	# 		page_num = 1

# 	# for each page
# 	for i in range(1, page_num+1):

# 		try:
# 			page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" + str(i) + "&q=" + author + "&utf8=%E2%9C%93")
# 			soup = BeautifulSoup(page.text, 'html.parser')
# 		except:
# 			print("could not connect to goodreads")
# 			break
			
# 		try:
# 			quote = soup.find(class_="leftContainer")
# 			quote_list = quote.find_all(class_="quoteDetails")
# 		except:
# 			pass
		
# 		#quote OOP turn metadata into a class itself or method
# 		# get data for each quote
# 		for quote in quote_list:

# 			meta_data = {"text": None, "author": None, "title": None, "tags": [], "timestamp": None}

# 			# Get quote's text
# 			try:
# 				outer = quote.find(class_="quoteText")
# 				# print(outer.text)
# 				inner_text = [element.strip() for element in outer if isinstance(element, NavigableString)]
# 				# print(inner_text)
# 				new_quote = ""
# 				for i in range(len(inner_text)):
# 					if '“' in inner_text[i] or '”' in inner_text[i]:
# 						new_quote += inner_text[i] + " "
# 				# print(new_quote)
# 				meta_data["text"] = new_quote
# 			except:
# 				pass

# 			# Get quote's author
# 			try:
# 				author = quote.find(class_="authorOrTitle").text
# 				author = author.replace(",", "")
# 				author = author.replace("\n", "")
# 				meta_data["author"] = author.strip()
# 				# print(author)
# 			except:
# 				pass

# 			# Get quote's book title
# 			try: 
# 				title = quote.find(class_="authorOrTitle")
# 				title = title.nextSibling.nextSibling.text
# 				title = title.replace("\n", "")
# 				meta_data["title"] =  title.strip()
# 				# print(title)
# 			except:
# 				pass

# 			# Get quote's tags
# 			try:
# 				tags = quote.find(class_="greyText smallText left").text
# 				tags = [x.strip() for x in tags.split(',')]
# 				tags = tags[1:]
# 				meta_data["tags"] = tags
# 				# print(tags)
# 			except:
# 				pass

# 			all_quotes.append(meta_data)
	

# 	return all_quotes



# quotes_by_author("william burroughs", 1)
