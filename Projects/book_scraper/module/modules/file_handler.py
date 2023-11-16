import os
import json


class FileHandler:
    """
    Handles all operations with files,
    including reading and writing data to and from files.
    """

    @staticmethod
    def read_wanted_books_json(filename):
        """
        Reads the titles of the books
        the user wants to get from a JSON file
        :param filename: str
        :return: list
        """
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"There has been an error when reading the file: {filename} ")

        with open(filename) as json_file:
            titles = json.load(json_file)
            return titles

    @staticmethod
    def save_to_json_file(filename, sorted_books_list):
        """
        Saving the sorted data into a json file, where they are
        grouped by predicate and order.
        :param filename: str
        :param sorted_books_list: list of tuples
        :return:
        """
        with open(filename, "w", encoding='utf-8') as json_file:
            for json_data, sort_predicate, sort_order in sorted_books_list:
                sort_order = sort_order or "ascending"
                sort_predicate = sort_predicate or "default"
                json_file.write(f"Sortings used : {sort_predicate} {sort_order}")
                json_file.write(json_data)
                json_file.write("------------------------------------\n")

    @staticmethod
    def convert_to_json(sorted_books_list):
        """
        Converts the books scraped into
        JSON format.
        :return: list of tuples
        """
        json_data_with_sorting_details = []
        books_dict_list = []

        for sorted_books, sort_predicate, sort_order in sorted_books_list:
            books_dict_list.clear()

            for book in sorted_books:
                books_dict = {
                    "title": book.title,
                    "genre": book.genre,
                    "price": book.price,
                    "availability": book.availability,
                    "rating": book.rating,
                    "description": book.description,
                    "product_info": book.product_info
                }
                books_dict_list.append(books_dict)

            json_data = json.dumps(books_dict_list, indent=2, ensure_ascii=False)
            json_data_with_sorting_details.append((json_data, sort_predicate, sort_order))
        FileHandler.save_to_json_file("results.json", json_data_with_sorting_details)
        return json_data_with_sorting_details

    @staticmethod
    def json_load(json_data):
        """
        Loads json data.
        :param: json_data: str
        :return: list of dictionaries
        """
        return json.loads(json_data)
