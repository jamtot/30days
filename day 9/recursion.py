"""Get the factorial of N using a recursive function."""
def factorial(number):
    """Recursively gets the factor of number."""
    if number > 1:
        return factorial(number - 1) * number
    return 1

if __name__ == '__main__':
    NUM = int(input())

    print(factorial(NUM))
