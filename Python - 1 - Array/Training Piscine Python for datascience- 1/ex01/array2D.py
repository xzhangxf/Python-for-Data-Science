import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version
    based on the provided start and end arguments using slicing.

    Args:
        family: 2D list representing the array to slice
        start: Starting index for slicing
        end: Ending index for slicing

    Returns:
        Truncated 2D list

    Raises:
        TypeError: If family is not a list or contains invalid types
        ValueError: If the 2D array rows have different lengths
        TypeError: If start or end are not integers
    """
    # Check if family is a list
    if not isinstance(family, list):
        raise TypeError("Family must be a list")

    # Check if start and end are integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")

    # Check if family is not empty
    if len(family) == 0:
        raise ValueError("Family list cannot be empty")

    # Check if all elements are lists (2D structure)
    for row in family:
        if not isinstance(row, list):
            raise TypeError("All elements in family must be lists")

    # Check if all rows have the same length
    if len(family) > 0:
        first_row_length = len(family[0])
        for row in family:
            if len(row) != first_row_length:
                raise ValueError("All rows must have the same length")

    # Check if all elements in rows are numbers
    for row in family:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("All elements must be int or float")

    # Convert to numpy array to get shape
    array = np.array(family)

    # Print original shape
    print(f"My shape is : {array.shape}")

    # Slice the array
    sliced_array = array[start:end]

    # Print new shape
    print(f"My new shape is : {sliced_array.shape}")

    # Convert back to list and return
    return sliced_array.tolist()


def main():
    """Main function for testing the slice_me function."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
