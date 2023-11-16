import requests


class HTTPRequest:
    @staticmethod
    def create_request(url):
        """
        Makes an HTTP request and returns
        the response from it
        :param url: str
        :return: Response object
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError:
            return None
