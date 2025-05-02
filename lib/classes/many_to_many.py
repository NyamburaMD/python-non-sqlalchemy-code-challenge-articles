from collections import Counter
class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        magazine.articles_list.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        pass
        
        
class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("The magazine must be an instance of Magazine.")
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = list({article.magazine.category for article in self.articles()})
        return None if not areas else areas

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self.articles_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
       

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if not value:
            raise ValueError("Category cannot be empty")
        self._category = value

    def articles(self):
        """Returns all articles associated with this magazine."""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Returns a list of unique contributors to this magazine."""
        return list({article.author for article in self.articles()})

    def article_titles(self):
        """Returns the titles of all articles in this magazine."""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """Returns authors who have contributed more than 2 articles to this magazine."""
        authors = [article.author for article in self.articles()]
        author_counts = Counter(authors)
        qualifying_authors = [author for author, count in author_counts.items() if count > 2]
        return qualifying_authors if qualifying_authors else None
    
    def check_name(self):
        """Validates the magazine's name."""
        if not isinstance(self._name, str) or not (2 <= len(self._name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")