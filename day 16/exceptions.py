"""Convert a string input to an integer, or throw an exception."""

if __name__ == "__main__":
    S = input().strip()

    try:
        print(int(S))
    except ValueError:
        print("Bad String")
