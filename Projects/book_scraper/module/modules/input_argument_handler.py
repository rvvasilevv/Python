import argparse
from module.modules.validate_input_data import (ValidateJsonFile, ValidateSorting, ValidateNumBooks,
                                                ValidateMultipleStringsIntoOne, ValidateFilters)


class InputArgumentHandler:
    """
    Handles all command line arguments
    and provides access to them
    """

    def __init__(self):
        """
        Initializes all field of the
        object by calling the correct
        object methods
        :param: __parsed_arguments: dictionary
        :param: __args_dict: dictionary
        :return:
        """
        self.__parsed_arguments = self.__parse_arguments()
        self.__args_dict = self.__create_args_dictionary()

    @staticmethod
    def __parse_arguments():
        """
        Define every possible argument
        and their respective restrictions.
        :return: dictionary
        """
        parser = argparse.ArgumentParser(description="Books Scraper")
        group = parser.add_mutually_exclusive_group(required=True)

        group.add_argument('-b', '--num_of_books', dest='books', type=int,
                           action=ValidateNumBooks,
                           help='Number of books')
        group.add_argument('-t', '--title', nargs='+', dest='title', type=str,
                           action=ValidateMultipleStringsIntoOne,
                           help='Search for a book title (only one)')
        group.add_argument('-w', '--books_from_json', dest='json_file_path',
                           action=ValidateJsonFile,
                           help='Search using a list of wanted books from JSON file')

        parser.add_argument('-g', '--genres', dest='genre', type=str, nargs='+',
                            help='List of genres to search through')
        parser.add_argument('-s', '--sortings', dest='sort', type=str, nargs='+', default=[(None, None)],
                            action=ValidateSorting,
                            help='Sorting predicate(s) and order(s) (e.g., rating ascending price descending)')
        parser.add_argument('-f', '--filters', dest='filter', type=str,
                            action=ValidateFilters,
                            help='List of filters')
        parser.add_argument('-d', '--keywords_in_description', nargs='+', dest='keyword_desc', type=str,
                            action=ValidateMultipleStringsIntoOne,
                            help='List of keywords for searching in the description')

        args = parser.parse_args()

        return args

    def __create_args_dictionary(self):
        """
        Creates a dictionary from all the
        passed in command line arguments
        and returns it
        :return: dictionary
        """
        arg_dict = {
            'num_books': self.__parsed_arguments.books,
            'genres': self.__parsed_arguments.genre,
            'filters': self.__parsed_arguments.filter,
            'keywords': self.__parsed_arguments.keyword_desc,
            'title_search': self.__parsed_arguments.title,
            'wanted_books_json': self.__parsed_arguments.json_file_path,
            'sorting_criteria': self.__parsed_arguments.sort
        }

        return arg_dict

    @property
    def args_dict(self):
        """
        Getter for args_dict
        :return: dictionary
        """
        return self.__args_dict
