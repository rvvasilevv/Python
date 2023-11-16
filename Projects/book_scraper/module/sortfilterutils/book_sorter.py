class BookSorter:
    """
    Responsible for sorting the books
    by varius fields
    """
    def __init__(self, books, default_sort_predicate):
        """
        Takes in the books to sort and the
        predicate by which they're to be sorted
        :param books: list
        :param default_sort_predicate: str
        """
        self.books = books
        self.default_sort_predicate = default_sort_predicate

    def sort_books(self, sort_predicate, sort_order):
        """
        Sorts the books in either ascending or descending order
        :param sort_predicate: str
        :param sort_order: str
        :return: list
        """
        #self.default_sort_predicate)

        sort_functions = {
            'rating': lambda book: book.rating,
            'price': lambda book: book.price,
            'availability': lambda book: book.availability,
            'title': lambda book: book.title,
        }

        def custom_key(book):
            if sort_predicate == self.default_sort_predicate or sort_predicate is None:
                return sort_functions[self.default_sort_predicate](book)
            primary_key = sort_functions.get(sort_predicate)(book)
            secondary_key = sort_functions[self.default_sort_predicate](book)
            return primary_key, secondary_key

        return sorted(self.books, key=custom_key, reverse=(sort_order == 'descending'))
