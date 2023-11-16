import unittest
from module.modules.scraper import BookScraper
from module.modules.book import Book


class TestScraper(unittest.TestCase):
    """
    Test BookScraper class
    """
    def setUp(self):
        """
        Set up data used for testing purposes.
        """
        self.test_books = [
            Book(title="Behind Closed Doors", genre="Thriller", price=52.22, availability=18, rating="Four",
                 description="Nice book", product_info={}),
            Book(title="Set Me Free", genre="Non-Young Adult", price=17.46, availability=19, rating="Five",
                 description="Nice book", product_info={}),
            Book(title="Mrs. Houdini", genre="Historical Fiction", price=30.25, availability=15, rating="Three",
                 description="Nice book", product_info={}),
            Book(title="The Kite Runner", genre="Default", price=41.82, availability=11, rating="Two",
                 description="Nice book", product_info={}),
            Book(title="Eight Hundred Grapes", genre="Fiction", price=14.39, availability=14, rating="One",
                 description="Nice book", product_info={}),
            Book(title="Alice in Wonderland", genre="Fiction", price=99.99, availability=19, rating="Three",
                 description="Nice book", product_info={})
        ]

    def test_scraper_with_title(self):
        """
        Test scraper with title.
        """
        args_with_title = {'num_books': None,
                           'genres': None,
                           'filters': None,
                           'keywords': None,
                           'title_search': "Behind Closed Doors",
                           'wanted_books_json': None,
                           'sorting_criteria': None}
        scraper = BookScraper(args_with_title)
        self.assertEqual(self.test_books[0].title, scraper.books[0].title, "fetch_book_info is not working")

    def test_scraper_with_genre(self):
        """
        Test scraper with genre.
        """
        args_with_genre = {'num_books': None,
                           'genres': ["Default", "Fiction"],
                           'filters': None,
                           'keywords': None,
                           'title_search': "The Kite Runner",
                           'wanted_books_json': None,
                           'sorting_criteria': None}
        scraper = BookScraper(args_with_genre)
        self.assertEqual(self.test_books[3].title,
                         scraper.books[0].title), "fetch_book_info is not working with genres"

    def test_scraper_with_no_valid_results(self):
        """
        Test scraper with no valid results.
        """
        args_with_no_output = {'num_books': None,
                               'genres': ["Fiction"],
                               'filters': None,
                               'keywords': None,
                               'title_search': "The Kite Runner",
                               'wanted_books_json': None,
                               'sorting_criteria': None}
        with self.assertRaises(ValueError):
            BookScraper(args_with_no_output)

    def test_scraper_with_json_titles(self):
        """
        Test scraper with json titles.
        """
        args_with_json_titles = {'num_books': None,
                                 'genres': None,
                                 'filters': None,
                                 'keywords': None,
                                 'title_search': None,
                                 'wanted_books_json': "test/jsonfiletests/testing.json",
                                 'sorting_criteria': None}
        scraper = BookScraper(args_with_json_titles)
        self.assertEqual(self.test_books[0].title,
                         scraper.books[0].title), "fetch_book_info is not working with titles from json file"