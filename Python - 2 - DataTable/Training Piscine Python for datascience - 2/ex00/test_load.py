#!/usr/bin/env python3

from ex03.load_csv import load


def test_load_csv():
    """Test the load function with various scenarios."""

    print("Testing load_csv function...")

    print("\n1. Testing with non-existent file:")
    result = load("nonexistent.csv")
    print(f"Result: {result}")

    print("\n2. Function import test:")
    print("Function imported successfully")
    print("Function can be called without syntax errors")

    print("\n3. Loading 'life_expectancy_year.csv':")
    df = load("life_expectancy_year.csv")
    print(df)

    print("\n4. Loading 'life_expectancy_years.csv':")
    df2 = load("life_expectancy_years.csv")
    print(df2)

    print("\nAll tests completed!")


if __name__ == "__main__":

    test_load_csv()
