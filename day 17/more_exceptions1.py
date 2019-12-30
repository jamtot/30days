"""Raise exceptions when numbers or exponents are negative."""

class NegativeException(Exception):
    """Raise for a negative number passed to power class."""

class Calculator(): #pylint:disable=too-few-public-methods
    """Calculator contains the power method."""

    def power(self, number, power_by): #pylint:disable=no-self-use
        """If neither input is negative returns n to the power of p."""
        if number | power_by < 0:
            raise NegativeException("n and p should be non-negative")
        return number**power_by

if __name__ == "__main__":
    MY_CALCULATOR = Calculator()
    T = int(input())
    for i in range(T):
        num, pow_r = map(int, input().split())
        try:
            ans = MY_CALCULATOR.power(num, pow_r)
            print(ans)
        except NegativeException as exception:
            print(exception)
