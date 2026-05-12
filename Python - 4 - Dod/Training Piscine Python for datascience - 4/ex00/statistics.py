from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''Calculate and print statistical measures based
    on input data and requested statistics.'''
    if len(args) == 0:
        print("ERROR")
        return

    data = list(args)

    def mean():
        '''Calculate the mean of the data.'''
        return float(sum(data)) / len(data)

    def median():
        '''Calculate the median of the data.'''
        s = sorted(data)
        n = len(s)
        mid = n // 2
        if n % 2 == 0:
            return (s[mid - 1] + s[mid]) / 2.0
        return s[mid]

    def quartile():
        '''Calculate the first and third
        quartiles of the data.'''
        s = sorted(data)
        q1 = s[len(s) // 4]
        q3 = s[(3 * len(s)) // 4]
        return [float(q1), float(q3)]

    def var():
        '''Calculate the variance of the data.'''
        m = mean()
        return sum((x - m) ** 2 for x in data) / len(data)

    def std():
        '''Calculate the standard deviation of the data.'''
        return var() ** 0.5

    funcs = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var,
    }

    for _, val in kwargs.items():
        if val in funcs:
            print(f"{val} : {funcs[val]()}")
        else:
            print("ERROR")
