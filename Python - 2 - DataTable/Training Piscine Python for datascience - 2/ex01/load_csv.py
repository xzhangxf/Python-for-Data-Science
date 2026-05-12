import pandas as pd


def load(path: str):
    """
    Load a CSV file and return it as a pandas DataFrame.
    Args:
        path (str): Path to the CSV file
    Returns:
        pandas.DataFrame or None: The loaded dataset or None if an error occurs
    """
    # Function body starts here
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Could not parse file '{path}'.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
