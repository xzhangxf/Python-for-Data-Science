import sys  # Importing the sys module to access command line arguments


def main():
    try:
        if len(sys.argv) == 1:
            # argv is a list of command line arguments,/
            # the first being the script name
            return
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        # when python raise it stop execution of the program\
        # and prints the errror meassage
        # raise is used to raise an exception if the condition\
        # is not met
        # AssertionError is build in python excpyion
        # lstrip("-") removes leading hyphens from the string
        # isdigit() checks if the string consists only of digits
        x = sys.argv[1]
        if not x.lstrip("-").isdigit():
            raise AssertionError("argument is not a number")
        x = int(x)
        if x % 2 == 0:
            print("I'm even.")
        else:
            print("I'm odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
# The main function checks if a command line argument is provided,\
# validates it as an integer, and prints whether it is even or odd.
