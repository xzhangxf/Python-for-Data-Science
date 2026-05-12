def ft_filter(function, iterable):
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


"""Construct an iterator from those elements of iterable for which\
    function returns true."""
