"""Check for whether a number is prime or not."""
import math

def check_prime(number):
    """Check obvious primes, then iterate through."""
    output = "Prime"
    if number == 2:
        return output
    if number < 2 or number % 2 == 0:
        return "Not p" + output[1:]
    for i in range(3, int(math.sqrt(float(number)))+1, 2):
        if number % i == 0:
            return "Not p" + output[1:]
    return output

if __name__ == "__main__":
    TESTS = int(input())
    for _ in range(TESTS):
        NUMBER = int(input())
        print(check_prime(NUMBER))
