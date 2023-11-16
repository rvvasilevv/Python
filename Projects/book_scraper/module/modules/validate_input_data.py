import argparse
import os
import re


class ValidateSorting(argparse.Action):
    """
    Validates the arguments for the sorting
    command line arguments
    """

    def __call__(self, parser, namespace, values, option_string=None):
        """
        Checks whether the fields
        and sorting order by which
        the books are being sorted
        are valid
        :param parser:
        :param namespace:
        :param values:
        :param option_string:
        :return:
        """
        valid_predicates = ('title', 'price', 'rating', 'availability')
        valid_order = ('ascending', 'descending')

        sorting_args = []

        for i in range(0, len(values), 2):
            predicate = values[i].lower()
            if i + 1 < len(values):
                order = values[i + 1]
            else:
                raise argparse.ArgumentError(self, f"Missing sorting order for {predicate}")

            if predicate not in valid_predicates:
                raise argparse.ArgumentError(self, f"{predicate} is not a valid sorting predicate")

            if order not in valid_order:
                raise argparse.ArgumentError(self, f"{order} is not a valid sorting order")

            sorting_args.append((predicate, order))

        setattr(namespace, self.dest, sorting_args)


class ValidateNumBooks(argparse.Action):
    """
    Validates the number of books argument
    """

    def __call__(self, parser, namespace, values, option_string=None):
        """
        Ensure that -b is grater than or equal to 0
        :param parser:
        :param namespace:
        :param values:
        :param option_string:
        :return:
        """
        num_books = values
        if int(num_books) <= 0:
            raise argparse.ArgumentError(self, "Number of books cannot be less than or equal to 0.")
        setattr(namespace, self.dest, num_books)


class ValidateJsonFile(argparse.Action):
    """
    Validates the path to the JSON file given
    """

    def __call__(self, parser, namespace, values, option_string=None):
        """
        Make sure that the path is to a valid JSON file
        :param parser:
        :param namespace:
        :param values:
        :param option_string:
        :return:
        """
        json_file_path = values
        if json_file_path:
            file_extension = os.path.splitext(json_file_path)[1]
            if file_extension.lower() != ".json":
                raise argparse.ArgumentError(self, f"The specified file '{json_file_path}' is not a JSON file.")
        setattr(namespace, self.dest, json_file_path)


class ValidateMultipleStringsIntoOne(argparse.Action):
    """
    Joins arguments passed separately into one string
    """

    def __call__(self, parser, namespace, values, option_string=None):
        """
        Joins arguments passed separately into one string
        :param parser:
        :param namespace:
        :param values:
        :param option_string:
        :return:
        """
        setattr(namespace, self.dest, ' '.join(values))


class ValidateFilters(argparse.Action):
    """
    Make sure that all filters given a valid
    """

    def __call__(self, parser, namespace, values, option_string=None):
        """
        Ensure that books are being
        filtered based on valid fields
        and values
        :param parser:
        :param namespace:
        :param values:
        :param option_string:
        :return:
        """
        predicates = values.replace(' ', '').lower().split(',')
        valid_filtering_criteria = ['price', 'availability', 'rating']

        valid_filters = []
        for predicate in predicates:
            operators = re.findall('<=|>=|<|>|=', predicate)
            if not operators:
                raise argparse.ArgumentTypeError("Invalid operator")

            parts = re.split('(<=|>=|<|>|=)', predicate)
            if len(parts) != 3:
                raise argparse.ArgumentTypeError(f"Invalid filter format: {predicate}. A filter must consist of a "
                                                 f"filtering criteria, an operator and a number")

            field, comparison, value = parts

            if field not in valid_filtering_criteria:
                raise argparse.ArgumentTypeError(f"Invalid filtering criteria: {field}")

            try:
                value = float(value)
            except ValueError:
                raise argparse.ArgumentTypeError(f"Invalid value: {value} (must be a number)")

            valid_filters.append((field, comparison, value))

        setattr(namespace, self.dest, valid_filters)
