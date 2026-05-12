import sys
import string


def count(text):

    total = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    punctuation = sum(1 for c in text if c in string.punctuation)
    space = sum(1 for c in text if c.isspace())
    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")


def main():
    try:
        if len(sys.argv) == 1:
            try:
                text = raw_input("What is the text to count?\n")
            except NameError:
                text = input("What is the text to count?\n")
            count(text)
        elif len(sys.argv) == 2:
            count(sys.argv[1])
        else:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
