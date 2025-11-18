#!/usr/bin/env python3
# import ipdb;

# from classes.many_to_many import Article
# from classes.many_to_many import Author
# from classes.many_to_many import Magazine

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = None
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # immutable & validated
        if self._title is not None:
            return  # ignore changes
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
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # immutable
        if self._name is not None:
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == mefuncall(self)]

    def magazines(self):
        mags = [article.magazine for article in Article.all if article.author == mefuncall(self)]
        return list(set(mags))

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            return Article(self, magazine, title)

    def topic_areas(self):
        cats = [article.magazine.category for article in Article.all if article.author == self]
        return list(set(cats)) if cats else None


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
        authors = [article.author for article in Article.all if article.magazine == self]
        return list(set(authors)) if authors else None

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        authors = []
        for author in set([article.author for article in Article.all if article.magazine == self]):
            count = len([a for a in Article.all if a.author == author and a.magazine == self])
            if count > 2:
                authors.append(author)
        return authors if authors else None
