## CHECK YOUR HEAD

For a daily dose of thought provoking quotes from writers, thinkers and artists that have shaped your life or ones who may in the future. This app will provide you with quotes from the Good Reads website, via scraping with a custom database compiled with authors and titles you choose.


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




### Project Status

The core functionality of this program is to webscrape text data from the GoodReads quote section of the website. The second part of it's functionality is to provide a random quote back to the user, which is timestamped and will not come across a duplicate quote for another 80 calls.