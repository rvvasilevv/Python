import unittest
from unittest.mock import patch
from module.modules.update_gsheet import UpdateGSheet


class TestUpdateGSheet(unittest.TestCase):
    """
    Test GSheet class functionality
    """
    @patch('gspread.authorize')
    @patch('gspread.spreadsheet')
    def setUp(self, mock_spreadsheet, mock_authorize):
        """
        Generate GSheet instance
        :param: mock_spreadsheet: Mock object
        :param: mock_authorize: Mock object
        """
        self.mock_gc = mock_authorize
        self.mock_spreadsheet = mock_spreadsheet
        self.sorted_book_data_json = [
            ('[{"title": "Book 1"}]', "title", "ascending"),
            ('[{"title": "Book 2"}]', "title", "descending")
        ]

        self.args = {
            'num_books': 10,
            'genres': ['Fiction', 'Mystery'],
            'sorting_criteria': 'title_ascending'
        }

        self.num_of_rows = 10
        self.test_gsheet = UpdateGSheet('Test Spreadsheet', 'test/jsonfiletests/test_credentials.json',
                                        self.sorted_book_data_json, self.args, self.num_of_rows)

    def test_clear_previous_data(self):
        """
        Test for the clear previous date in GSheet functionality
        """
        self.mock_spreadsheet.reset_mock()
        self.test_gsheet._clear_previous_data()
        self.assertEqual(self.mock_spreadsheet.del_worksheet.call_count, len(self.mock_spreadsheet.worksheets()))

    def test_add_result_to_main_worksheet(self):
        """
        Test for the add result to main worksheet functionality
        """
        self.mock_spreadsheet.reset_mock()
        self.assertEqual(self.test_gsheet._add_result_to_main_worksheet(self.args, "title",  "ascending"), 'Results2')

    def test_create_data_to_insert_in_the_sheet(self):
        """
        Test for creating data to insert in the sheet functionality
        """
        json_data = [
            {"Title": "Book 1", "Author": "Author 1", "Price": "$10.00", "Rating": "4.5"},
            {"Title": "Book 2", "Author": "Author 2", "Price": "$12.00", "Rating": "4.7"},
        ]
        expected_data = [
            ["Title", "Author", "Price", "Rating"],
            ["Book 1", "Author 1", "$10.00", "4.5"],
            ["Book 2", "Author 2", "$12.00", "4.7"],
        ]
        self.assertEqual(self.test_gsheet._create_data_to_insert_in_the_sheet(json_data), expected_data)

