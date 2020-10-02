## CHECK YOUR HEAD

For a daily dose of thought provoking quotes from writers, thinkers and artists that have shaped your life or ones who may in the future. This app will provide you with quotes from the Good Reads website, via scraping with a custom database compiled with authors and titles you choose. You can access this database that will return a random quote from the library, with minimum repeats.


### Installation



### Usage

Upon running main.py, the user will be prompted with 3 options.

```
1 - Add an author/title
2 - Get a random quote
3 - Exit 
```

If user selects option 1, they will be asked to provide the name or title. This function is not case sensitive, and will provide feedback for source location.


```
What author or title would you like quotes from?
```

Once user has input the chosen author or title, the message below should appear.

```
Looking for quotes...
```
If the database was updated with content, the following message should appear.

```
Library updated!
```

If unsuccessful, the user should see this message.

```
Sorry, we did not recognise this author/title
```

If user selects option 2, and there is content within the database. It will return a quote from the JSON data file.

```
“The narcotic tobacco haze of Capitalism”  

- Allen Ginsberg
```

If there is no data in the JSON file, the following error message should occur, followed by the menu prompt to select an option.

```
Your database is empty, please add an author or title.

What would you like to do?

        1 - Add author or title
        2 - Get me a random quote
        3 - Exit

Select: 
```

If user selects option 3, a message will be printed to the screen and the program will exit.

```
Thank you for using Check Your Head!
```

If the user would like to stop the function, they can use KeyboardInterrupt command (ctrl + c) to stop the program.


### Development Overview

This application returns printed quotes from a locally stored database of user chosen authors and titles from the Good Reads website via a web scraper.  

The functions of this applications are:

**Web scraping data**
This is done via GET request to the URL of the quotes section of the Good Reads website.

**Storing data in local database**
This is a personal library that will allow the application to select a random quote from, and print it to the user screen.

**Select and print random quote**
The function allows the user to print a random quote from their database which will not allow the quote to be printed again for at least 30 days. This function exists to allow the app to be built upon, and for any developer interested in connecting an SMS or email API that will allow the quotes to be sent to a device of their choice.

#### How

The application begins by presenting the user with a selection of choices to determine what function they would like to execute.

This is executed with equality logical operators, which will prevent the user from selecting invalid keys.

```
1 - Add author or title
2 - Get me a random quote
3 - Exit
```

Without a local database already created, the user will not be able to receive a random quote. This is done by the message presented

### Project Status

The core functionality of this program is to webscrape text data from the GoodReads quote section of the website. The second part of it's functionality is to provide a random quote back to the user, which is timestamped and will not come across a duplicate quote for another 80 calls.