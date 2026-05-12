def square(x: int | float) -> int | float:
    '''Return the square of a number.'''
    return x * x


def pow(x: int | float) -> int | float:
    '''Return the power of a number.'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''Return a counter function that applies
    the given function.'''
    count = 0

    def inner() -> float:
        nonlocal count, x
        count += 1
        x = function(x)
        return x
    return inner
