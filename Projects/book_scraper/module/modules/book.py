class Book:
    """
    Models the books being scraped
    """

    __slots__ = ('__title', '__genre', '__price', '__availability', '__rating', '__description', '__product_info')

    def __init__(self, title, genre, price, availability, rating, description, product_info):
        """
        Initialize all the fields of the book object
        :param title: str
        :param genre: str
        :param price: float
        :param availability: int
        :param rating: str
        :param description: str
        :param product_info: dic
        """
        self.title = title
        self.genre = genre
        self.price = price
        self.availability = availability
        self.rating = rating
        self.description = description
        self.product_info = product_info

    @property
    def title(self):
        """
        Get the __title field
        :return: str
        """
        return self.__title

    @title.setter
    def title(self, value):
        """
        Set the __title field
        :param value: str
        :return:
        """
        self.__title = value

    @property
    def genre(self):
        """
        Get the __genre field
        :return: str
        """
        return self.__genre

    @genre.setter
    def genre(self, value):
        """
        Set the __genre field
        :param value: str
        :return:
        """
        self.__genre = value

    @property
    def price(self):
        """
        Get the __price field
        :return: float
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Set the __price field
        :param value: float
        :return:
        """
        self.__price = value

    @property
    def availability(self):
        """
        Get the __availability field
        :return: int
        """
        return self.__availability

    @availability.setter
    def availability(self, value):
        """
        Set the __availability field
        :param value: int
        :return:
        """
        self.__availability = value

    @property
    def rating(self):
        """
        Get the __rating field
        :return: int
        """
        return self.__rating

    @rating.setter
    def rating(self, value):
        """
        Set the __rating field
        :param value: str
        :return:
        """
        self.__rating = value

    @property
    def description(self):
        """
        Get the __description field
        :return: str
        """
        return self.__description

    @description.setter
    def description(self, value):
        """
        Set the __description field
        :param value: str
        :return:
        """
        self.__description = value

    @property
    def product_info(self):
        """
        Get the __product_info field
        :return: dic
        """
        return self.__product_info

    @product_info.setter
    def product_info(self, value):
        """
        Set the __product_info field
        :param value: dic
        :return:
        """
        self.__product_info = value
