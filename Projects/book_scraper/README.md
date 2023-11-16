# Web Scraper documentation

* ## Project Summary
This program provides a CLI for scraping the site
https://books.toscrape.com/ for the available book
data. The user can specify a variety of command line
arguments to filter and sort the data as they wish
after which the results are all saved within a JSON
file and also displayed in Google Sheets. 

* ## Requirements
This script is run using [python3](https://www.python.org/).  
The following modules are used as dependencies:
requests, beautifulsoup, gspread, oauth2client.  
Connection to the internet is required for this script to function.  
Google Sheet credentials in the form of a JSON file and rename it to credentials.json
need to be provided for proper authorization.
In order to obtain Google Sheets credentials, the user is required 
to create a ServiceNow account and enable Google Drive and Google Docs API.

For more detailed information, please refer to **[this guide](https://developers.google.com/workspace/guides/create-credentials)**.


* ## Usage
The script is used to gather data from https://books.toscrape.com/.
You can write the following command in your terminal:
  ```
  python main.py [-b <number of books>] [-g <list of genres>]
                 [-s <list of sortings>] [-f <list of filters>]
                 [-d <list of keywords>] [-t <book title>]
                 [-w <list of book titles>]
  ```
About the optional arguments:
  * -b number of books that are to be scraped
  * -g the book genres which are to be scraped
  * -s a list of sorting predicates and orders
  	
  	*Valid sorting predicates are: title, price, rating and availability*
  	
  	*Valid sorting orders are: ascending and descending* 
  	
  	
  * -f a list of criteria that the books must meet
  	
  	*Valid filtering criteria are: price, rating and availability*
  	
  	*Valid comparison operators are: <, <=, =, >=, >*
  	 
  	
  * -d keywords that must be present in the book's description
  * -t a book title (only one) to search for
  * -w a list of book titles to search for (from the given JSON
containing a list of book titles)

Note: The -b, -t and -w arguments are mutually exclusive,
exactly one of them must be provided
  
  
* ## Tests
The test subdirectory provides unit tests for each module that can be found
in the modules subdirectory.
  
* ## Technical Details
This program scrapes the available data for the books found on
https://books.toscrape.com/ using the requests library to make
the HTTP requests and the beautiful soup package to extract the
actual data.

Utilizing the argparse library the application provides a multitude
of command-line arguments that the user can input to specify 
exactly what they're looking for when it comes to books (i.e., the number of
books to be returned, genres of the books, exact values for specific
fields of the books, etc.)

After the user provides their search criteria the program begins
scraping the website for books that meet said criteria until all
conditions are satisfied or there are no more books left to scrape.
After which the results are sorted and saved both in Google Sheets
and locally in the form of a JSON file.
  
### Workflow:
To start the program the user must call it from the command line and
provide all arguments needed for the search. All passed arguments
must go through validation for the program to proceed with carrying out the
request.

Once all arguments are validated the program will begin scraping
the site until it has gathered all the necessary data to display. It will
only finish once one of three conditions has been met:  
1/ The number of books specified by the -b argument has been reached  
2/ All titles it is looking for (specified by the -t or -w argument) have
been found  
3/ There are no more books left to scrape

In the process of scraping, the scraper first identifies (if given the -g argument) all the genres it
is required to search through while scraping and filters the results based on any other given arguments 
it is trying to satisfy. After that, it begins asynchronously scraping book data while it
only adds valid (those that meet the search criteria) books to its list of
books. Once it's finished scraping, it returns the books sorted according to
all sorting predicates and orders that were passed in.
If multiple sorting predicates are given, the different sortings will be split into different results. The default predicate and order will be used if no sorting predicates are given.

Finally, the results returned by the scraper are saved in the form of a JSON file and
uploaded to Google Sheets using the credentials that the user has supplied
through the credentials.json file.

### Testing:
Currently, all modules are being tested and the coverage is 96%.

