"""Inheritance is explored through example.

A person class uses a first and last name, and ID.
A student class inherits from the person class, but
adds test scores, and a function to output a grade based
on their average test scores.
"""

class Person:  # pylint: disable=too-few-public-methods
    """Person class, has name and ID."""

    def __init__(self, first_name, last_name, id_number):
        """Initialise the class's variables."""
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
    def print_person(self):
        """Print the person's name and ID."""
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)

class Student(Person):
    """Inherits from person class, adds test scores."""

    def __init__(self, first_name, last_name, id_number, scores):
        """Initialise the parent class, and the scores."""
        super().__init__(first_name, last_name, id_number)
        self.test_scores = scores

    def calculate(self):
        """Calculate the grade based on average scores."""
        count = len(self.test_scores)
        average = (sum(self.test_scores) / count)

        grade = 'T'
        if average >= 90:
            grade = 'O'
        elif average >= 80:
            grade = 'E'
        elif average >= 70:
            grade = 'A'
        elif average >= 55:
            grade = 'P'
        elif average >= 40:
            grade = 'D'
        return grade

if __name__ == "__main__":
    LINE = input().split()
    FIRST_NAME = LINE[0]
    LAST_NAME = LINE[1]
    ID_NUM = LINE[2]
    NUM_SCORES = int(input()) # not needed for Python
    SCORES = list(map(int, input().split()))
    STUDENT = Student(FIRST_NAME, LAST_NAME, ID_NUM, SCORES)
    STUDENT.print_person()
    print("Grade:", STUDENT.calculate())
