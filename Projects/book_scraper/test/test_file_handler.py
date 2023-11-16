import io
import unittest
from unittest.mock import patch

from module.modules.book import Book
from module.modules.file_handler import json, FileHandler


class TestFileHandlerClass(unittest.TestCase):
    """
    Test FileHandler functionality
    """
    def setUp(self):
        """
        Set up FileHandler object and generate sample book to use afterward for testing purposes
        """
        self.test_file_handler = FileHandler()
        self.books = [
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

    def test_read_wanted_books_json(self):
        """
        Test the functionality for reading the wanted books json(base test)
        """
        self.assertEqual(self.test_file_handler.read_wanted_books_json('test/jsonfiletests/testing.json'), [
            "Behind Closed Doors"])

    def test_read_wanted_books_json_with_empty_file(self):
        """
        Test the functionality for reading the wanted books json(test with empty json file)
        """
        with self.assertRaises(json.JSONDecodeError):
            self.test_file_handler.read_wanted_books_json('test/jsonfiletests/empty.json')

    def test_read_wanted_books_json_with_nonexistent_file(self):
        """
        Test the functionality for reading the wanted books json(test with nonexistent json file)
        """
        with self.assertRaises(FileNotFoundError):
            self.test_file_handler.read_wanted_books_json('test/jsonfiletests/books.json')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_save_to_json_file(self, mock_stdout):
        """
        Test the save to json functionality
        """
        json_data = [
                ('{"title": "Book 1"}', "title", "ascending"),
                ('{"title": "Book 2"}', "title", "descending")
            ]

        expected_output = (
            'Sortings used : title ascending'
            '{"title": "Book 1"}'
            '------------------------------------\n'
            'Sortings used : title descending'
            '{"title": "Book 2"}'
            '------------------------------------\n'
        )

        self.test_file_handler.save_to_json_file('test/jsonfiletests/output.json', json_data)

        with open('test/jsonfiletests/output.json', 'r', encoding='utf-8') as json_file:
            saved_content = json_file.read()

        self.assertEqual(saved_content, expected_output)

    def test_scraper_convert_to_json(self):
        """
        Test the conversion to json functionality
        """
        test_sorted_books = [(self.books, "rating", "ascending")]
        result = self.test_file_handler.convert_to_json(test_sorted_books)
        self.assertIsInstance(result, list)




