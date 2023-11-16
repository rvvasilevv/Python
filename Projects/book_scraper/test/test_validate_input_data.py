import argparse
import unittest
from module.modules.validate_input_data import (ValidateJsonFile, ValidateSorting, ValidateNumBooks,
                                                ValidateMultipleStringsIntoOne, ValidateFilters)


class TestValidationClasses(unittest.TestCase):
    """
    Testing all the validation classes, which inherit the argparse.Action class and are used as an action parameter.
    """

    def test_valid_sorting(self):
        """
        Testing validation of sorting arguments with correct values.
        """
        parser = argparse.ArgumentParser()
        action = ValidateSorting(option_strings=['--sortings'], dest='sort')
        namespace = argparse.Namespace()
        valid_sorting_args = ['title', 'ascending', 'price', 'descending']
        action(parser, namespace, valid_sorting_args)
        self.assertEqual(namespace.sort, [('title', 'ascending'), ('price', 'descending')])

    def test_invalid_sorting_predicate(self):
        """
        Testing validation of sorting arguments with incorrect values.
        """
        parser = argparse.ArgumentParser()
        action = ValidateSorting(option_strings=['--sortings'], dest='sort')
        namespace = argparse.Namespace()
        invalid_sorting_args = ['invalid_predicate', 'ascending']
        with self.assertRaises(argparse.ArgumentError):
            action(parser, namespace, invalid_sorting_args)

    def test_invalid_sorting_order(self):
        """
        Testing validation of sorting arguments with incorrect sorting order.
        """
        parser = argparse.ArgumentParser()
        action = ValidateSorting(option_strings=['--sortings'], dest='sort')
        namespace = argparse.Namespace()
        invalid_sorting_args = ['title', 'invalid_order']
        with self.assertRaises(argparse.ArgumentError):
            action(parser, namespace, invalid_sorting_args)

    def test_invalid_number_of_sorting_criteria(self):
        """
        Testing validation of sorting arguments with incorrect number of sorting criteria.
        """
        parser = argparse.ArgumentParser()
        action = ValidateSorting(option_strings=['--sortings'], dest='sort')
        namespace = argparse.Namespace()
        invalid_sorting_args = ['title', 'ascending', 'price']
        with self.assertRaises(argparse.ArgumentError):
            action(parser, namespace, invalid_sorting_args)

    def test_valid_num_books(self):
        """
        Test validation of number of books argument with valid number.
        """
        parser = argparse.ArgumentParser()
        action = ValidateNumBooks(option_strings=['--num_of_books'], dest='books')
        namespace = argparse.Namespace()
        valid_num_books = 10
        action(parser, namespace, valid_num_books)
        self.assertEqual(namespace.books, valid_num_books)

    def test_invalid_num_books(self):
        """
        Test validation of number of books with an invalid number.
        """
        parser = argparse.ArgumentParser()
        action = ValidateNumBooks(option_strings=['--num_of_books'], dest='books')
        namespace = argparse.Namespace()
        invalid_num_books = -5
        with self.assertRaises(argparse.ArgumentError):
            action(parser, namespace, invalid_num_books)

    def test_invalid_num_books_zero(self):
        """
        Test validation of number of books with an invalid number, which is an edge case: 0.
        """
        parser = argparse.ArgumentParser()
        action = ValidateNumBooks(option_strings=['--num_of_books'], dest='books')
        namespace = argparse.Namespace()
        invalid_num_books = 0
        with self.assertRaises(argparse.ArgumentError):
            action(parser, namespace, invalid_num_books)

    def test_valid_json_file(self):
        """
        Test validation of -w argument with a valid argument.
        """
        parser = argparse.ArgumentParser()
        action = ValidateJsonFile(option_strings=['--books_from_json'], dest='json_file_path')
        namespace = argparse.Namespace()
        valid_json_file = 'books.json'
        action(parser, namespace, valid_json_file)
        self.assertEqual(namespace.json_file_path, valid_json_file)

    def test_valid_json_file_in_caps(self):
        """
        Test validation of -w argument with a valid argument, which extension is in caps.
        """
        parser = argparse.ArgumentParser()
        action = ValidateJsonFile(option_strings=['--books_from_json'], dest='json_file_path')
        namespace = argparse.Namespace()
        valid_json_file = 'books.JSON'
        action(parser, namespace, valid_json_file)
        self.assertEqual(namespace.json_file_path, valid_json_file)

    def test_invalid_json_file_extension(self):
        """
        Test validation of -w argument with an invalid argument, which does not end in .json.
        """
        parser = argparse.ArgumentParser()
        action = ValidateJsonFile(option_strings=['--books_from_json'], dest='json_file_path')
        namespace = argparse.Namespace()
        invalid_json_file = 'books.txt'
        with self.assertRaises(argparse.ArgumentError):
            action(parser, namespace, invalid_json_file)

    def test_valid_multiple_strings_into_one(self):
        """
        Test validation of creating a string from a list of strings when taking arguments.
        """
        parser = argparse.ArgumentParser()
        action = ValidateMultipleStringsIntoOne(option_strings=['--keywords_in_description'], dest='keyword_desc')
        namespace = argparse.Namespace()
        valid_strings = ['word1', 'word2', 'word3']
        action(parser, namespace, valid_strings)
        self.assertEqual(namespace.keyword_desc, 'word1 word2 word3')

    def test_valid_filters(self):
        """
        Test validation of filter argument with valid data.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        valid_filters = 'price<=10,rating>4,availability=1.0'
        action(parser, namespace, valid_filters)
        expected_result = [
            ('price', '<=', 10.0),
            ('rating', '>', 4.0),
            ('availability', '=', 1.0)
        ]
        self.assertEqual(namespace.filter, expected_result)

    def test_invalid_filter_format(self):
        """
        Test validation of filter argument with an invalid data.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        invalid_filters = 'invalid_format'
        with self.assertRaises(argparse.ArgumentTypeError):
            action(parser, namespace, invalid_filters)

    def test_invalid_filter_field(self):
        """
        Test validation of filter argument with an invalid field.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        invalid_filters = 'invalid_field=10'
        with self.assertRaises(argparse.ArgumentTypeError):
            action(parser, namespace, invalid_filters)

    def test_invalid_filter_value(self):
        """
        Test validation of filter argument with an invalid value.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        invalid_filters = 'price=invalid_value'
        with self.assertRaises(argparse.ArgumentTypeError):
            action(parser, namespace, invalid_filters)

    def test_empty_filter(self):
        """
        Test validation of filter argument with an empty value.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        empty_filters = ''
        with self.assertRaises(argparse.ArgumentTypeError):
            action(parser, namespace, empty_filters)

    def test_valid_whitespace_in_filter(self):
        """
        Test validation of filter argument with valid filters containing whitespace.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        valid_filters = 'price <= 10.0, availability > 1, rating >= 3.5'
        action(parser, namespace, valid_filters)
        expected_result = [
            ('price', '<=', 10.0),
            ('availability', '>', 1.0),
            ('rating', '>=', 3.5)
        ]
        self.assertEqual(namespace.filter, expected_result)

    def test_valid_filter_operator(self):
        """
        Test validation of filter argument with valid operator.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        valid_filters = 'price<=10.0, availability>1, rating=3.5, rating>=4.0, price<5.0'
        action(parser, namespace, valid_filters)
        expected_result = [
            ('price', '<=', 10.0),
            ('availability', '>', 1.0),
            ('rating', '=', 3.5),
            ('rating', '>=', 4.0),
            ('price', '<', 5.0)
        ]
        self.assertEqual(namespace.filter, expected_result)

    def test_invalid_filter_operator(self):
        """
        Test validation of filter argument with an invalid operator.
        """
        parser = argparse.ArgumentParser()
        action = ValidateFilters(option_strings=['--filters'], dest='filter')
        namespace = argparse.Namespace()
        invalid_filters = 'price!=10.0'
        with self.assertRaises(argparse.ArgumentTypeError):
            action(parser, namespace, invalid_filters)
