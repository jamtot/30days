"""Implement an abstract class Book."""

from abc import ABCMeta, abstractmethod

class Book(metaclass=ABCMeta): # pylint: disable=too-few-public-methods
    """Contains title, author, and abstract displayb function."""

    def __init__(self, title, author):
        """Initialise the title and author."""
        self.title = title
        self.author = author
    @abstractmethod
    def display(): # pylint: disable=no-method-argument
        """Abstract display method with no implementation."""
        pass # pylint: disable=unnecessary-pass

class MyBook(Book): # pylint: disable=too-few-public-methods
    """Implementation of abstract class Book."""

    def __init__(self, title, author, price):
        """Call the base class constructor and set price."""
        super().__init__(title, author)
        self.price = price

    def display(self):
        """Display function implementation."""
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))

if __name__ == "__main__":
    TITLE = input()
    AUTHOR = input()
    PRICE = int(input())
    NEW_NOVEL = MyBook(TITLE, AUTHOR, PRICE)
    NEW_NOVEL.display()
