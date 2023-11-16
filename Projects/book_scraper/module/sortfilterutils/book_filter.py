class BookFilter:
    """
    Handles the process of filtering
    the book data according to given
    criteria
    """
    @staticmethod
    def filter_by_description(description, keywords):
        """
        Filters the description according the
        keywords it's supposed to contain
        :param description: str
        :param keywords: str
        :return: bool
        """
        if not keywords:
            return True
        list_of_words_to_search = keywords.split(" ")
        counter = 0
        for keyword in list_of_words_to_search:
            if keyword.lower() in description.lower():
                counter += 1
        return counter == len(list_of_words_to_search)

    @staticmethod
    def filter_by_genre(soup, genres):
        """
        Finds the links to the genres
        from which books are to be scraped
        :param soup: str
        :param genres: list of str
        :return: list of str
        """
        genre_links_to_search = []
        nav_list = soup.find('ul', class_="nav nav-list")
        available_genres_in_page = nav_list.find_all('a', href=True)
        available_genres_in_page = {genre.get_text(strip=True).lower(): genre['href'] for genre in
                                    available_genres_in_page}

        for genre in genres:
            if genre.lower() in available_genres_in_page:
                genre_links_to_search.append(available_genres_in_page[genre.lower()])
            else:
                print(f"There is no such genre as {genre}")

        if genre_links_to_search:
            return genre_links_to_search
        else:
            raise ValueError(f"There are no such genres as: {genres}")

    @staticmethod
    def search_book_by_title(books, titles_to_search):
        """
        Gets the book titles and links
        for all books on the page
        :param books: str
        :param titles_to_search: list
        :return: dictionary
        """
        books_in_current_page = {}
        found_books = {}
        for h3_element in books:
            a_element = h3_element.find('a', {'title': True})
            if a_element:
                book_title = a_element.get('title').lower()
                href_element = a_element.get('href')
                books_in_current_page[book_title] = href_element
        for title in titles_to_search:
            if title.lower() in books_in_current_page:
                found_books[title] = books_in_current_page[title.lower()]

        return found_books

    @staticmethod
    def filter(price, availability, rating, filters):
        """
        Filters the fields of a book and
        returns True if they match all filters
        :param price: float
        :param availability: int
        :param rating: int
        :param filters: list
        :return: bool
        """
        if not filters:
            return True

        filtering_criteria = {
            'price': float(price[1:]),
            'availability': availability,
            'rating': rating,
        }

        comparisons = {
            '<': lambda f, v: filtering_criteria[f] < v,
            '=': lambda f, v: filtering_criteria[f] == v,
            '>': lambda f, v: filtering_criteria[f] > v,
            '<=': lambda f, v: filtering_criteria[f] <= v,
            '>=': lambda f, v: filtering_criteria[f] >= v,
        }
        counter = 0
        for predicate in filters:
            criteria, comparison, value = predicate
            if comparisons[comparison](criteria, value):
                counter += 1
        return counter == len(filters)
