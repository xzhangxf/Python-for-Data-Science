def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
        return 0
    elif isinstance(object, float) and str(object == "nan"):
        print("Cheese: nan <class 'float'>")
        return 0
    elif object == 0 and isinstance(object, int):
        print("Zero: 0 <class 'int'>")
        return 0
    elif isinstance(object, str) and object == '':
        print("Empty: <class 'str'>")
        return 0
    elif isinstance(object, bool) and object is False:
        print("Fake: False <class 'bool'>")
        return 0
    else:
        print("Type not found")
        return 1

# The function NULL_not_found checks the type of the input object
# and prints a message based on its type.
# If the object is None, it prints "Nothing: None <class 'NoneType'>".
# If the object is a float and is NaN, it prints "Cheese: nan
# <class 'float'>".
# If the object is an integer and is 0, it prints "Zero: 0
# <class 'int'>".
# If the object is a string and is empty, it prints "Empty:
# <class 'str'>".
# If the object is a boolean and is False, it prints "Fake: False
# <class 'bool'>".
# If the object does not match any of these conditions, it prints
# "Type not found".
# The function returns 0 for the first five cases and 1 for the
# last case.
# The function is used to identify and handle specific types of
# objects, particularly those that represent "null" or "not found"
# values.
# The function is useful for debugging or validating input data
# types in a program.
# The function can be extended to handle more types or specific
# cases as needed.


# why will have ___pycache__ in the folder?
#  The __pycache__ directory is created by Python to store compiled
# bytecode files (.pyc) for modules that have been imported.
#  This allows Python to load modules faster in subsequent runs,
# as it can skip the compilation step if the source code hasn't
# changed.

# 1. __pycache__ is only created when you import a module
# If you only ran a script like this:
# python NULL_not_found.py
# And did not import anything, then no __pycache__ is created.
# But now you're doing this in tester.py:
# from NULL_not_found import NULL_not_found
# That’s an import, so Python compiles NULL_not_found.py into
# bytecode and saves it as:
# __pycache__/NULL_not_found.cpython-XXX.pyc

# 2. Running scripts directly doesn't always create bytecode
# If you run a script directly (like python myscript.py), Python
# doesn’t always cache it unless:
# The script is imported as a module, or
# You're using some interactive environments like REPL or Jupyter
