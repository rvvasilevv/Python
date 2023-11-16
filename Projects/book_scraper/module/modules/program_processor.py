from module.modules.input_argument_handler import InputArgumentHandler
from module.modules.scraper import BookScraper
from module.modules.update_gsheet import UpdateGSheet
from module.modules.file_handler import FileHandler


class ProgramProcessor:
    """
    The class responsible for managing
    all other classes in program.
    """

    SPREADSHEET_TITLE = "DataScraper"
    CREDENTIALS_TITLE = "credentials.json"

    def __call__(self):
        """
        Runs all the processes needed for
        to complete the user's request in
        the correct order.
        """
        parser = InputArgumentHandler()
        args = parser.args_dict
        scraper = BookScraper(args)
        all_sorted_results = scraper.create_sorted_books_list(default_sort_predicate='price')
        sorted_book_data_json = FileHandler.convert_to_json(all_sorted_results)
        UpdateGSheet(self.SPREADSHEET_TITLE, self.CREDENTIALS_TITLE, sorted_book_data_json, args, len(scraper.books)+1)
