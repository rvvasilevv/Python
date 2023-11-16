import threading as t
import time
from bs4 import BeautifulSoup
from module.modules.book import Book
from module.sortfilterutils.book_filter import BookFilter
from module.sortfilterutils.book_sorter import BookSorter
from module.modules.file_handler import FileHandler
from module.modules.http_request import HTTPRequest


class BookScraper:
    """
    Handles all the logic related to
    scraping the book data from the website.
    """

    BASE_URL = "http://books.toscrape.com/catalogue/page-1.html"
    REQUIRED_URL_PART = 36
    RATING_MAP = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, args):
        """
        Initializes all the fields that will
        be necessary in order to correctly scrape
        all the desired data.
        :param args: dictionary
        """
        self.args = args
        self.books = []
        self.titles_from_json = []
        self.__num_of_books_to_scrape = 0
        self.__books_titles_to_search = []
        self.__book_threads = []
        self.__lock = t.Lock()
        self.__set_search_type()
        self.__scrape_books()

    def __set_search_type(self):
        """
        Set the type of searching used for the scraper.
        :return:
        """
        self.__num_of_books_to_scrape = self.__args['num_books'] or float('inf')
        self.__books_titles_to_search = [self.__args['title_search']] if self.__args['title_search'] else []
        if self.__args['wanted_books_json']:
            self.__titles_from_json = FileHandler.read_wanted_books_json(self.__args["wanted_books_json"])
            self.__books_titles_to_search.extend(self.__titles_from_json)

    def __scrape_books(self):
        """
        Main method used to scrape all
        books that meet the criteria we
        are looking for.
        :return:
        """
        result = HTTPRequest.create_request(self.BASE_URL)
        if result is None:
            raise ConnectionError(f"Site couldn't be reached: {self.BASE_URL}")

        soup = BeautifulSoup(result.content.decode('utf-8', 'ignore'), 'html.parser')

        if self.__args['genres']:
            genres_links = BookFilter.filter_by_genre(soup, self.__args['genres'])
            self.__search_books_by_genre(genres_links)
        else:
            self.__load_page(self.BASE_URL)

        if len(self.__books) == 0:
            raise ValueError("The 'books' list is empty. This means that no books match your criteria."
                             " Cannot create sorted list.")

    def __load_page(self, page_url):
        """
        Loads pages from the website
        that contain books listed on them.
        :param page_url: str
        :return:
        """
        while page_url:
            result = HTTPRequest.create_request(page_url)
            if result is None:
                raise ConnectionError(f"Site couldn't be reached: {page_url}")

            soup = BeautifulSoup(result.content.decode('utf-8', 'ignore'), 'html.parser')
            html_books_in_current_page = soup.find_all('h3')

            if self.__args['wanted_books_json'] or self.__args['title_search']:
                if not len(self.__books) != len(self.__books_titles_to_search):
                    break
                self.__search_books_by_title(html_books_in_current_page)

            else:
                self.__scrape_books_by_number(html_books_in_current_page)

            next_button = soup.find('li', class_='next')

            if not next_button or not len(self.__books) < self.__num_of_books_to_scrape:
                break

            next_page_relative_url = next_button.a.get('href')
            page_url = page_url + "/../" + next_page_relative_url

    def fetch_book_info(self, book_url):
        """
        Scrapes the data from a given book's
        page and returns it.
        :param book_url: str
        :return:
        """
        response = HTTPRequest.create_request(book_url)
        if response is None:
            raise ConnectionError(f"Site couldn't be reached: {book_url}")
        soup = BeautifulSoup(response.content.decode('utf-8', 'ignore'), 'html.parser')

        title, genre, price, availability, rating, description, product_info = self.__extract_book_data(soup)

        if not (BookFilter.filter(price, availability, rating, self.__args['filters']) &
                BookFilter.filter_by_description(description, self.__args['keywords'])):
            return None

        with self.__lock:
            if self.__num_of_books_to_scrape is not None and len(self.__books) >= self.__num_of_books_to_scrape:
                return None
            self.__books.append(Book(title, genre, price, availability, rating, description, product_info))
        return None

    def __scrape_books_by_number(self, books):
        """
        Scrapes a given number of books
        :param books: list
        :return:
        """
        for book in books:
            book_url = book.a['href']
            book_page = self.BASE_URL[:self.REQUIRED_URL_PART:] + book_url
            actual_book_page = book_page.replace("../../../", '')
            thread = t.Thread(target=self.fetch_book_info, args=(actual_book_page,))
            thread.start()
            time.sleep(0.03)  # we are delaying the threads to ensure the proper order of the books
            self.__book_threads.append(thread)

        for thread in self.__book_threads:
            thread.join()

    def __search_books_by_genre(self, genre_links):
        """
        Searches for books in the given links to
        the book genres we're looking for
        :param genre_links: list of str
        :return:
        """
        for link in genre_links:
            page_url = self.BASE_URL[:self.REQUIRED_URL_PART:] + link
            self.__load_page(page_url)

    def __search_books_by_title(self, html_books):
        """
        Searches for all books that have the
        titles we are looking for
        :param html_books: list of str
        :return:
        """
        found_titles_dict = BookFilter.search_book_by_title(html_books, self.__books_titles_to_search)
        for book in found_titles_dict:
            url = found_titles_dict[book]
            book_page_url = self.BASE_URL[:self.REQUIRED_URL_PART:] + url
            page_to_use = book_page_url.replace("../../../", '')
            self.fetch_book_info(page_to_use)

    def create_sorted_books_list(self, default_sort_predicate):
        """
        Sorts the books based on the specified sorting criteria.
        :return: A list of tuples containing the sorted book, predicate and order used.
        """
        sorter = BookSorter(self.__books, default_sort_predicate=default_sort_predicate)
        all_sorted_results = []

        for sort_predicate, sort_order in self.__args['sorting_criteria']:
            copy_of_sorted_books = sorter.sort_books(sort_predicate, sort_order)
            all_sorted_results.append((copy_of_sorted_books, sort_predicate, sort_order))

        return all_sorted_results

    @staticmethod
    def __extract_book_data(soup):
        """
        Extract needed book data from the html into needed types.
        :param: soup: str
        """
        title = soup.h1.text.strip()
        genre = soup.select('ul.breadcrumb li')[-2].text.strip()
        price = soup.select_one('p.price_color').text.strip()
        availability = int(''.join(filter(str.isdigit, soup.select_one('p.availability').text.strip())))
        rating_string = soup.select('p.star-rating')[0]['class'][1]
        rating_number = BookScraper.__convert_rating_str_to_int(rating_string)

        description = ' '.join(soup.find('meta', {'name': 'description'})['content'].split())
        product_info = {}
        table = soup.find('table', class_='table-striped')

        rows = table.find_all('tr')
        for row in rows:
            header = row.find('th')
            data = row.find('td')
            key = header.text.strip()
            value = data.text.strip()
            product_info[key] = value

        return title, genre, price, availability, rating_number, description, product_info

    @staticmethod
    def __convert_rating_str_to_int(rating_string):
        """
        Convert the rating string into a number.
        :param: rating_string: str
        :return: rating_map[rating_string]
        """
        if rating_string not in BookScraper.RATING_MAP:
            raise ValueError(f"Invalid rating value: {rating_string}. The supported rating is from 1 to 5.")
        return BookScraper.RATING_MAP[rating_string]

    @property
    def args(self):
        """
        Gets the __args field
        :return: dictionary
        """
        return self.__args

    @args.setter
    def args(self, value):
        """
        Sets the __args field
        :param value: dictionary
        :return:
        """
        self.__args = value

    @property
    def books(self):
        """
        Gets the __books field
        :return: list
        """
        return self.__books

    @books.setter
    def books(self, value):
        """
        Sets the __books field
        :param value: list
        :return:
        """
        self.__books = value

    @property
    def titles_from_json(self):
        """
        Gets the __titles_from_json field
        :return: list
        """
        return self.__titles_from_json

    @titles_from_json.setter
    def titles_from_json(self, value):
        """
        Sets the __titles_from_json field
        :param value: list
        :return:
        """
        self.__titles_from_json = value
