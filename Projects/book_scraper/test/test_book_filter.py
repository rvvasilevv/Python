import unittest
from io import StringIO
from bs4 import BeautifulSoup
from module.sortfilterutils.book_filter import BookFilter


class TestBookFilter(unittest.TestCase):
    """
    Testing the Book Filter class.
    """

    def setUp(self):
        """
        Opening the sample html page and grabbing the elements of the books
        """
        with open("test/sample_page_html/main_page.html", "rb") as file:
            self.saved_html = file.read()
        self.soup = BeautifulSoup(self.saved_html, 'html.parser')
        self.html_books_in_current_page = self.soup.find_all('h3')

    def test_filter_by_description_single_present_keyword(self):
        """
        Test the filter by description and whether it will find the keyword.
        """
        description = "A great book with useful information"
        keywords = "great"
        result = BookFilter.filter_by_description(description, keywords)
        self.assertTrue(result)

    def test_filter_by_description_multiple_present_keywords(self):
        """
        Test the filter by description and whether it will find multiple keywords.
        """
        description = "A great book with useful information"
        keywords = "great useful"
        result = BookFilter.filter_by_description(description, keywords)
        self.assertTrue(result)

    def test_filter_by_description_single_non_present_keyword(self):
        """
        Test the filter by description with keyword non-present in the description.
        """
        description = "A great book with useful information"
        keywords = "non-present"
        result = BookFilter.filter_by_description(description, keywords)
        self.assertFalse(result)

    def test_filter_by_description_multiple_keywords_but_not_all_of_them_present(self):
        """
        Test the filter by description with multiple keywords but not all of them being present in the description.
        """
        description = "A great book with useful information"
        keywords = "great, non-present"
        result = BookFilter.filter_by_description(description, keywords)
        self.assertFalse(result)

    def test_filter_by_price_below(self):
        """
        Test filtering by price below a certain value.
        """
        filters = [('price', '<', 25.0)]
        result = BookFilter.filter(price="$17.46", availability=19, rating=5, filters=filters)
        self.assertTrue(result)

    def test_filter_by_price_above(self):
        """
        Test filtering by price above a certain value.
        """
        filters = [('price', '>', 25.0)]
        result = BookFilter.filter(price="$52.22", availability=18, rating=5, filters=filters)
        self.assertTrue(result)

    def test_filter_by_price_equal(self):
        """
        Test filtering by price equal to a certain value.
        """
        filters = [('price', '=', 30.25)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_price_above_or_equal(self):
        """
        Test filtering by price above or equal to a certain value.
        """
        filters = [('price', '>=', 30.25)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_price_below_or_equal(self):
        """
        Test filtering by price below or equal to a certain value.
        """
        filters = [('price', '<=', 30.25)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_rating_below(self):
        """
        Test filtering by rating below a certain value.
        """
        filters = [('rating', '<', 3)]
        result = BookFilter.filter(price="$17.46", availability=19, rating=1, filters=filters)
        self.assertTrue(result)

    def test_filter_by_rating_above(self):
        """
        Test filtering by rating above a certain value.
        """
        filters = [('rating', '>', 2)]
        result = BookFilter.filter(price="$52.22", availability=18, rating=5, filters=filters)
        self.assertTrue(result)

    def test_filter_by_rating_equal(self):
        """
        Test filtering by rating equal to a certain value.
        """
        filters = [('rating', '=', 3)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_rating_above_or_equal(self):
        """
        Test filtering by rating above or equal to a certain value.
        """
        filters = [('rating', '>=', 3)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_rating_below_or_equal(self):
        """
        Test filtering by rating below or equal to a certain value.
        """
        filters = [('rating', '<=', 3)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_availability_below(self):
        """
        Test filtering by availability below a certain value.
        """
        filters = [('availability', '<', 23)]
        result = BookFilter.filter(price="$17.46", availability=19, rating=1, filters=filters)
        self.assertTrue(result)

    def test_filter_by_availability_above(self):
        """
        Test filtering by availability above a certain value.
        """
        filters = [('rating', '>', 2)]
        result = BookFilter.filter(price="$52.22", availability=18, rating=5, filters=filters)
        self.assertTrue(result)

    def test_filter_by_availability_equal(self):
        """
        Test filtering by availability equal to a certain value.
        """
        filters = [('availability', '=', 15)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_availability_above_or_equal(self):
        """
        Test filtering by availability above or equal to a certain value.
        """
        filters = [('availability', '>=', 15)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_availability_below_or_equal(self):
        """
        Test filtering by availability below or equal to a certain value.
        """
        filters = [('availability', '<=', 15)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=3, filters=filters)
        self.assertTrue(result)

    def test_filter_by_multiple_met_filters(self):
        """
        Test filtering by multiple filter with met conditions.
        """
        filters = [('availability', '<=', 15), ('rating', '=', 5)]
        result = BookFilter.filter(price="$30.25", availability=15, rating=5, filters=filters)
        self.assertTrue(result)

    def test_filter_by_multiple_non_met_filters(self):
        """
        Test filtering by multiple filters, which conditions are not met.
        """
        filters = [('availability', '<=', 15), ('rating', '=', 5)]
        result = BookFilter.filter(price="$30.25", availability=14, rating=4, filters=filters)
        self.assertFalse(result)

    def test_filter_by_multiple_filters_not_all_met(self):
        """
        Test filtering by multiple filters, some of which the object meets the condition and some of which it doesn't.
        """
        filters = [('availability', '<=', 15), ('rating', '=', 5)]
        result = BookFilter.filter(price="$30.25", availability=16, rating=5, filters=filters)
        self.assertFalse(result)

    def test_single_book_title_present_in_the_page(self):
        """
        Test searching for a single book title that is present in the html books.
        """
        titles_to_search = ['A Light in the Attic']
        result = BookFilter.search_book_by_title(self.html_books_in_current_page, titles_to_search)
        self.assertEqual(result, {'A Light in the Attic': 'a-light-in-the-attic_1000/index.html'})

    def test_multiple_book_titles_present_in_the_page(self):
        """
        Test searching for multiple book titles that are present in the html books.
        """
        multiple_titles_to_search = ['A Light in the Attic', 'Olio']
        result = BookFilter.search_book_by_title(self.html_books_in_current_page, multiple_titles_to_search)
        self.assertEqual(result, {'A Light in the Attic': 'a-light-in-the-attic_1000/index.html',
                                  'Olio': 'olio_984/index.html'})

    def test_single_book_title_not_present_in_the_page(self):
        """
        Test searching for a single book title that is not present in the html books.
        """
        titles_to_search = ["Non-Existent Book"]
        result = BookFilter.search_book_by_title(self.html_books_in_current_page, titles_to_search)
        self.assertEqual(result, {})

    def test_multiple_book_titles_not_present_in_the_page(self):
        """
        Test searching for multiple book titles, none of which are present in the html books.
        """
        multiple_titles_to_search = ["Non", "Existing", "Book"]
        result = BookFilter.search_book_by_title(self.html_books_in_current_page, multiple_titles_to_search)
        self.assertEqual(result, {})

    def test_present_and_non_present_book_titles_in_the_page(self):
        """
        Test searching for multiple book titles, some of which are present and some of which are not.
        """
        multiple_titles_to_search = ['A Light in the Attic', "Does not Exist"]
        result = BookFilter.search_book_by_title(self.html_books_in_current_page, multiple_titles_to_search)
        self.assertEqual(result, {'A Light in the Attic': 'a-light-in-the-attic_1000/index.html'})

    def test_filter_by_genre_all_matching_genres(self):
        """
        Test the filter_by_genre method with all matching genres.
        """
        genres = ["Fiction", "Mystery"]
        result = BookFilter.filter_by_genre(self.soup, genres)
        self.assertEqual(len(result), 2)

    def test_filter_by_genre_partial_matching_genres(self):
        """
        Test the filter_by_genre method with some matching and some non-matching genres.
        """
        genres = ["Fiction", "Non-Existent Genre", "Mystery"]
        result = BookFilter.filter_by_genre(self.soup, genres)
        self.assertEqual(len(result), 2)

    def test_filter_by_genre_no_matching_genres(self):
        """
        Test the filter_by_genre method with genres that are not present in the HTML page.
        """
        genres = ["No", "Matches"]
        with self.assertRaises(ValueError):
            BookFilter.filter_by_genre(self.soup, genres)

    def test_filter_by_genre_unmatched_genre_prints_message(self):
        """
        Test if the filter_by_genre method prints a message for an unmatched genre.
        """
        genres = ["Fiction", "Non-Existent Genre"]
        with StringIO() as mock_output:
            import sys
            original_stdout = sys.stdout
            sys.stdout = mock_output
            BookFilter.filter_by_genre(self.soup, genres)
            sys.stdout = original_stdout
            self.assertIn("There is no such genre as", mock_output.getvalue())
