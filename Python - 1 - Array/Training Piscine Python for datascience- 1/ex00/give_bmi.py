import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for given height and weight arrays.

    Args:
        height: List of heights in meters
        weight: List of weights in kilograms

    Returns:
        List of BMI values

    Raises:
        ValueError: If height and weight arrays have different lengths
        ValueError: If any height value is 0 or negative
        TypeError: If inputs are not lists or contain invalid types
    """
    # Check if inputs are lists
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists")

    # Check if lists have the same length
    if len(height) != len(weight):
        raise ValueError("Height and weight arrays must have the same length")

    # Check if all elements are int or float
    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("All height values must be int or float")

    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("All weight values must be int or float")

    # Check for positive height values
    if any(h <= 0 for h in height):
        raise ValueError("Height values must be positive")

    # Convert to numpy arrays for vectorized operations
    height_array = np.array(height)
    weight_array = np.array(weight)

    # Calculate BMI: weight / height^2
    bmi = weight_array / (height_array ** 2)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a BMI limit to determine if each BMI value is above the limit.

    Args:
        bmi: List of BMI values
        limit: BMI threshold value

    Returns:
        List of boolean values indicating if each BMI is above the limit

    Raises:
        TypeError: If inputs are not of correct types
    """
    # Check if bmi is a list
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list")

    # Check if limit is an integer
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")

    # Check if all BMI values are int or float
    for value in bmi:
        if not isinstance(value, (int, float)):
            raise TypeError("All BMI values must be int or float")

    return [value > limit for value in bmi]


def main():
    """Main function for testing the BMI functions."""
    # Test the functions
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    print("Height:", height)
    print("Weight:", weight)

    try:
        bmi = give_bmi(height, weight)
        print("BMI:", bmi)

        limit = 26
        result = apply_limit(bmi, limit)
        print(f"BMI > {limit}:", result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
