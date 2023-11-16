import unittest
from module.modules.scraper import HTTPRequest


class TestHTTPRequest(unittest.TestCase):
    """
    Test HTTP_Request class
    """

    def test_response(self):
        """
        Test if site is working.
        """
        url = "http://books.toscrape.com/catalogue/page-1.html"
        response = HTTPRequest.create_request(url)
        self.assertTrue(200 <= response.status_code < 300, "Site cannot be reached")
