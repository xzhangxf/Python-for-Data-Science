class calculator:
    '''calculator class that supports addition, subtraction,
    multiplication, and division operations on a list of numbers.'''
    def __init__(self, values):
        '''Initialize the calculator with a list of numbers.'''
        self.values = values

    def __add__(self, other):
        '''Add a number to each element in the list.'''
        result = [x + other for x in self.values]
        print(result)

    def __mul__(self, other):
        '''Multiply each element in the list by a number.'''
        result = [x * other for x in self.values]
        print(result)

    def __sub__(self, other):
        '''Subtract a number from each element in the list.'''
        result = [x - other for x in self.values]
        print(result)

    def __truediv__(self, other):
        '''Divide each element in the list by a number.'''
        if other == 0:
            print("Error: Division by zero.")
            return
        result = [x / other for x in self.values]
        print(result)
