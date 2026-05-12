from typing import Any


def callLimit(limit: int):
    """Return a decorator that allows calling the wrapped
    function at most `limit` times."""
    count = 0

    def callLimiter(function):
        """Decorator that enforces the call limit using a
        closure counter."""

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter
