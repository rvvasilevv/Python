import unittest
from io import StringIO
from unittest.mock import patch
from module.modules.input_argument_handler import InputArgumentHandler


class TestInputArgumentHandler(unittest.TestCase):
    """
    Testing the input class when providing command line arguments.
    """

    @patch('sys.argv', ['main.py', '-b', '5'])
    def test_num_books_argument(self):
        """
        Testing whether the -b argument is taken correctly.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['num_books'], 5)

    @patch('sys.argv', ['main.py', '-g', 'Fantasy', '-b', '50'])
    def test_single_genre_argument(self):
        """
        Testing whether the -g argument is taken correctly with a single genre.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['genres'], ['Fantasy'])

    @patch('sys.argv', ['main.py', '-g', 'Fantasy', 'Mystery', '-b', '50'])
    def test_multiple_genre_arguments(self):
        """
        Testing whether the -g argument is taken correctly with multiple genres.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['genres'], ['Fantasy', 'Mystery'])

    @patch('sys.argv', ['main.py', '-f', 'availability>15', '-b', '50'])
    def test_single_filter_argument(self):
        """
        Testing whether the -f argument is taken correctly with one filter.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['filters'], [('availability', '>', 15.0)])

    @patch('sys.argv', ['main.py', '-f', 'availability>15, rating<2', '-b', '50'])
    def test_multiple_filter_arguments(self):
        """
        Testing whether the -f argument is taken correctly with multiple filters.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['filters'], [('availability', '>', 15.0), ('rating', '<', 2.0)])

    @patch('sys.argv', ['main.py', '-w', 'test.json'])
    def test_wanted_books_json_argument(self):
        """
        Testing whether the -w argument is taken correctly
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['wanted_books_json'], 'test.json')

    @patch('sys.argv', ['main.py', '-d', 'love', '-b', '50'])
    def test_single_description_argument(self):
        """
        Testing whether the -d argument is taken correctly with a single keyword.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['keywords'], 'love')

    @patch('sys.argv', ['main.py', '-d', 'love', 'not', '-b', '50'])
    def test_multiple_description_arguments(self):
        """
        Testing whether the -d argument is taken correctly with multiple keywords.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['keywords'], 'love not')

    @patch('sys.argv', ['main.py', '-t', 'Set Me Free'])
    def test_title_search_argument(self):
        """
        Testing whether the -t argument is taken correctly
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['title_search'], 'Set Me Free')

    @patch('sys.argv', ['main.py', '-t', 'Set Me Free', '-s', 'rating', 'ascending'])
    def test_single_sorting_argument(self):
        """
        Testing whether the -s argument is taken correctly with a single predicate and order.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['sorting_criteria'], [('rating', 'ascending')])

    @patch('sys.argv', ['main.py', '-t', 'Set Me Free', '-s', 'rating', 'ascending', 'price', 'descending'])
    def test_multiple_sorting_arguments(self):
        """
        Testing whether the -s argument is taken correctly with a multiple predicates and orders.
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['sorting_criteria'], [('rating', 'ascending'),
                                                                       ('price', 'descending')])

    @patch('sys.argv', ['main.py', '-t', 'Set Me Free'])
    def test_sorting_default_values(self):
        """
        Testing whether the -s argument has the desired default values
        """
        input_handler = InputArgumentHandler()
        self.assertEqual(input_handler.args_dict['sorting_criteria'], [(None, None)])

    @patch('sys.argv', ['main.py', '-b', '5', '-w', 'test.json'])
    def test_mutually_exclusive_args_error(self):
        """
        Testing whether the mutually exclusive arguments work correctly and raise an error.
        """
        with self.assertRaises(SystemExit) as cm:
            InputArgumentHandler()
        self.assertEqual(cm.exception.code, 2)

    @patch('sys.argv', ['main.py', '--help'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_help_message(self, mock_stdout):
        """
        Testing whether the --help command will display the correct data.
        """
        with self.assertRaises(SystemExit) as cm:
            InputArgumentHandler()
        self.assertEqual(cm.exception.code, 0)
        help_output = mock_stdout.getvalue()
        self.assertIn("usage: main.py [-h] (-b BOOKS | -t TITLE [TITLE ...] | -w JSON_FILE_PATH)", help_output)
        self.assertIn("Books Scraper", help_output)
        self.assertIn("-b BOOKS, --num_of_books BOOKS", help_output)
        self.assertIn("-t TITLE [TITLE ...], --title TITLE [TITLE ...]", help_output)
        self.assertIn("-w JSON_FILE_PATH, --books_from_json JSON_FILE_PATH", help_output)
        self.assertIn("-g GENRE [GENRE ...], --genres GENRE [GENRE ...]", help_output)
        self.assertIn("-s SORT [SORT ...], --sortings SORT [SORT ...]", help_output)
        self.assertIn("-f FILTER, --filters FILTER", help_output)
        self.assertIn("-d KEYWORD_DESC [KEYWORD_DESC ...], --keywords_in_description KEYWORD_DESC [KEYWORD_DESC ...]",
                      help_output)

    @patch('sys.argv', ['main.py'])
    def test_no_arguments(self):
        """
        Test when no arguments are provided.
        """
        with self.assertRaises(SystemExit) as cm:
            InputArgumentHandler()
        self.assertEqual(cm.exception.code, 2)

    @patch('sys.argv', ['main.py', '-g', 'Fantasy', '-s', 'rating', 'ascending'])
    def test_missing_required_args(self):
        """
        Test when no required argument (-w, -t or -b) is provided.
        """
        with self.assertRaises(SystemExit) as cm:
            InputArgumentHandler()
        self.assertEqual(cm.exception.code, 2)
