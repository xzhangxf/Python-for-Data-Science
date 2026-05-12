import numpy as np
from PIL import Image
# PIL python imaging library
# which is allow to open manipulate and save many different image file formats
# is now maintained as a fork called pillow
# so from pil import image actully use pillow


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path and return it as a numpy array.
    Args:
        path: Path to the image file
    Returns:
        numpy.ndarray: The image as a numpy array
    Raises:
        FileNotFoundError: If the image file doesn't exist
        ValueError: If the file is not a valid image
        TypeError: If path is not a string
    grayscale image is a 2d arry(height, width)
    color image is a 3d array(height, width, channels)
    so imgae_array.shep = (400, 600, 3)
    400 pixels tall 600 pixels wide 3 color channels (RGB)
    graysclae channels is 1 rgb is 3 rgba is 4 transparency
    so if print(image_arry[0,0]) is the top left rgb color
    like [225, 255, 255]
    """
    # Check if path is a string
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    try:
        # Load the image using PIL
        image = Image.open(path)
        # Convert to numpy array
        image_array = np.array(image)
        # Print the shape of the image
        print(f"The shape of image is: {image_array.shape}")
        return image_array
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found: {path}")
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")


def main():
    """Main function for testing the ft_load function."""
    try:
        # Test loading the provided image
        image_path = "animal.jpeg"
        image_array = ft_load(image_path)
        print(f"Image loaded successfully with shape: {image_array.shape}")
        print(f"Image data type: {image_array.dtype}")

    except (FileNotFoundError, ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
