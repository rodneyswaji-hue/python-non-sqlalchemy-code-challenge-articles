class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = None
        self._author = None
        self._magazine = None

        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title is immutable (cannot be changed once set)
        if self._title is not None:
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name  # must validate on creation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Author name is immutable
        if self._name is not None:
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]


    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            return Article(self, magazine, title)

    def topic_areas(self):
        categories = {article.magazine.category for article in self.articles()}
        return list(categories) if categories else None


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None

        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles or None

    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            count = sum(1 for a in self.articles() if a.author == author)
            if count > 2:
                authors.append(author)
        return authors or None
