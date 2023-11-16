import unittest
from module.modules.book import Book
from module.sortfilterutils.book_sorter import BookSorter


class TestBookSorter(unittest.TestCase):
    """
    Test Book Sorter class.
    """

    def setUp(self):
        """
        Setting up a list of books used for testing purposes
        """
        self.books = [
            Book(title="Behind Closed Doors", genre="Thriller", price=52.22, availability=18, rating=4,
                 description="Nice book", product_info={}),
            Book(title="Set Me Free", genre="Non-Young Adult", price=17.46, availability=19, rating=5,
                 description="Nice book", product_info={}),
            Book(title="Mrs. Houdini", genre="Historical Fiction", price=30.25, availability=15, rating=3,
                 description="Nice book", product_info={}),
            Book(title="The Kite Runner", genre="Default", price=41.82, availability=11, rating=2,
                 description="Nice book", product_info={}),
            Book(title="Eight Hundred Grapes", genre="Fiction", price=14.39, availability=14, rating=1,
                 description="Nice book", product_info={}),
            Book(title="Alice in Wonderland", genre="Fiction", price=99.99, availability=19, rating=3,
                 description="Nice book", product_info={})
        ]

    def test_sort_books_by_price_ascending(self):
        """
        Test book sorting by price predicate, ascending order.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='price', sort_order='ascending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "Eight Hundred Grapes")  # Lowest price
        self.assertEqual(sorted_books[-1].title, "Alice in Wonderland")  # Highest price

    def test_sort_books_by_availability_ascending(self):
        """
        Test book sorting by availability predicate, ascending order.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='availability', sort_order='ascending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "The Kite Runner")  # Lowest availability
        self.assertEqual(sorted_books[-1].title, "Set Me Free")  # Highest availability

    def test_sort_books_by_title_ascending(self):
        """
        Test book sorting by title predicate, ascending order.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='title', sort_order='ascending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "Alice in Wonderland")  # Alphabetical order first title
        self.assertEqual(sorted_books[-1].title, "The Kite Runner")  # Alphabetical order last title

    def test_sort_books_by_rating_ascending(self):
        """
        Test book sorting by rating predicate, ascending order
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='rating', sort_order='ascending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "Eight Hundred Grapes")  # Lowest rating
        self.assertEqual(sorted_books[-1].title, "Set Me Free")  # Highest rating

    def test_sort_books_by_price_descending(self):
        """
        Test book sorting by price predicate, descending order.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='price', sort_order='descending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "Alice in Wonderland")  # Highest price
        self.assertEqual(sorted_books[-1].title, "Eight Hundred Grapes")  # Highest price

    def test_sort_books_by_availability_descending(self):
        """
        Test book sorting by availability predicate, descending order.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='availability', sort_order='descending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "Set Me Free")  # Highest availability
        self.assertEqual(sorted_books[-1].title, "The Kite Runner")  # Lowest availability

    def test_sort_books_by_rating_descending(self):
        """
        Test book sorting by rating predicate, descending order.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='rating', sort_order='descending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "Set Me Free")  # Highest rating
        self.assertEqual(sorted_books[-1].title, "Eight Hundred Grapes")  # Lowest rating

    def test_sort_books_by_title_descending(self):
        """
        Test book sorting by title predicate, descending order.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate='title', sort_order='descending')
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "The Kite Runner")  # Alphabetical order last title
        self.assertEqual(sorted_books[-1].title, "Alice in Wonderland")  # Alphabetical order first title

    def test_default_sorting_behavior(self):
        """
        Test default sorting behavior using None for sort_predicate and sort_order. This means that the sorting
        should be by the default sort_predicate given as an argument to the instance and
        the sort order should be ascending.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='rating')
        book_sorter.sort_books(sort_predicate=None, sort_order=None)
        sorted_books = book_sorter.books
        self.assertEqual(sorted_books[0].title, "Eight Hundred Grapes")  # Lowest rating
        self.assertEqual(sorted_books[-1].title, "Set Me Free")  # Highest rating

    def test_sorting_behaviour_with_same_values(self):
        """
        Test book sorting by a predicate and an order, when books have the same values for the predicate.
        Behaviour should be that the default predicate is taken into consideration when sorting those two books.
        """
        book_sorter = BookSorter(self.books, default_sort_predicate='price')
        book_sorter.sort_books(sort_predicate='availability', sort_order='descending')
        sorted_books = book_sorter.books
        # Books with the same availability should be sorted by the default predicate 'price' in descending order
        self.assertEqual(sorted_books[0].title, "Alice in Wonderland")  # availability: 19, price: 99.99
        self.assertEqual(sorted_books[1].title, "Set Me Free")  # availability: 19, price: 17.46
