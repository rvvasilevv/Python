import unittest
from module.modules.book import Book


class TestBookClass(unittest.TestCase):
    """
    Test book class functionality
    """
    def setUp(self):
        """
        Generate sample book to use afterward for testing purposes
        """
        self.test_book = Book(
            title="Sample Book",
            genre="Fiction",
            price=19.99,
            availability=10,
            rating=4,
            description="A sample book description",
            product_info={"UPC": "8a380641491d43ed", "Product Type": "Books", "Price (excl. tax)": "£56.76",
                          "Price (incl. tax)": "£56.76", "Tax": "£0.00", "Availability": "In stock (16 available)",
                          "Number of reviews": "0"})

    def test_title_property(self):
        """
        Test to check if the title is taken correctly
        """
        self.assertEqual(self.test_book.title, "Sample Book")

    def test_genre_property(self):
        """
        Test to check if the genre is taken correctly
        """
        self.assertEqual(self.test_book.genre, "Fiction")

    def test_price_property(self):
        """
        Test to check if the price is taken correctly
        """
        self.assertAlmostEqual(self.test_book.price, 19.99)

    def test_availability_property(self):
        """
        Test to check if the availability is taken correctly
        """
        self.assertEqual(self.test_book.availability, 10)

    def test_rating_property(self):
        """
        Test to check if the rating is taken correctly
        """
        self.assertEqual(self.test_book.rating, 4)

    def test_description_property(self):
        """
        Test to check if the description is taken correctly
        """
        self.assertEqual(self.test_book.description, "A sample book description")

    def test_product_info_property(self):
        """
        Test to check if the product info dictionary is taken correctly
        """
        self.assertEqual(self.test_book.product_info, {"UPC": "8a380641491d43ed", "Product Type": "Books",
                                                       "Price (excl. tax)": "£56.76", "Price (incl. tax)": "£56.76",
                                                       "Tax": "£0.00", "Availability": "In stock (16 available)",
                                                       "Number of reviews": "0"})
