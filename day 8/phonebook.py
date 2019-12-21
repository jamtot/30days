"""Create and query a rudimentary phonebook."""
import sys

def phonebook():
    """Return a phonebook.

    First take an integer representing
    the amount of names and numbers to be added.
    Then take that amount of lines with space-separated
    strings.
    """
    number = int(input())
    phone_book = dict()
    for _ in range(number):
        name, number = input().split()
        phone_book[name] = number
    return phone_book

def get_names():
    """Take in an unknown amount of names."""
    names = list()
    for line in sys.stdin:
        names.append(line.rstrip())
    return names

def query_phonebook(phone_book, names):
    """Query the phonebook with a list of names."""
    for name in names:
        if name in phone_book:
            print(name + "=" + phone_book[name])
        else:
            print("Not found")

if __name__ == "__main__":
    PHONE_BOOK = phonebook()
    NAMES = get_names()
    query_phonebook(PHONE_BOOK, NAMES)
