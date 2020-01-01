"""Exploring the use of interfaces, abstract class with no method implementations."""
import math

class AdvancedArithmetic(object): #pylint:disable=too-few-public-methods,useless-object-inheritance
    """Abstract class with a divisorSum(n) method with no implementation."""

    def divisor_sum(self, num):
        """Implement in a child class."""
        raise NotImplementedError

class Calculator(AdvancedArithmetic): #pylint:disable=too-few-public-methods
    """Calculator class implements the AdvancedArithmetic interface."""

    def divisor_sum(self, num):
        """Implement the interface above."""
        sum_div = 0
        sqr_t = int(math.sqrt(num))
        for i in range(1, sqr_t + 1):
            if num%i == 0:
                if num/i == i:
                    sum_div += i
                else:
                    sum_div += i + num / i
        return int(sum_div)

if __name__ == "__main__":
    NUMBER = int(input())
    MY_CALCULATOR = Calculator()
    SUM = MY_CALCULATOR.divisor_sum(NUMBER)
    print("I implemented: " + type(MY_CALCULATOR).__bases__[0].__name__)
    print(SUM)
