"""Review of previous days.

Take n amounts of string inputs and output
space seperated strings comprised of the odd
and even indices.
"""

def review(number):
    """Take n number of inputs and sort by index."""
    for _ in range(number):
        inp = input()
        lenp = len(inp)
        odd = ""
        even = ""
        for j in range(lenp):
            if j%2 == 1:
                odd += inp[j]
            else:
                even += inp[j]
        print(even+" "+odd)

if __name__ == "__main__":
    review(int(input()))
