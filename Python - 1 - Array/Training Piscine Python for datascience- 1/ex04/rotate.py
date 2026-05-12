import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from load_image import ft_load

matplotlib.use('TkAgg')  # Use WSL-compatible interactive backend


def zoom(image: np.ndarray) -> np.ndarray:
    """
    Zooms into the center of an image and converts it to grayscale.
    Returns a 400x400x1 grayscale numpy array.
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("Image must be a numpy array")

    height, width = image.shape[:2]
    if height < 400 or width < 400:
        raise ValueError("Image too small for 400x400 crop")

    # Crop 400x400 from center, adjusting for animal face
    # For a 768x1024 image, center is at (384, 512)
    start_row = height // 2 - 280  # Starting Y position: move 280 pixels up
    # Logic: height//2 = center Y, subtract to move UP in image
    end_row = start_row + 400       # Ending Y position: 400 pixels down
    # Logic: add 400 to get bottom edge of 400px tall crop
    start_col = width // 2 - 60    # Starting X position: move 60 pixels left
    # Logic: width//2 = center X, subtract to move LEFT from center
    end_col = start_col + 400       # Ending X position: 400 pixels right
    # Logic: add 400 to get right edge of 400px wide crop

    cropped = image[start_row:end_row, start_col:end_col]

    # Convert to grayscale and keep shape (400, 400, 1)
    grayscale = np.dot(cropped[..., :3], [0.2989, 0.5870, 0.1140])
    grayscale = grayscale[..., np.newaxis].astype(np.uint8)

    return grayscale


def rotate_90_ccw(image: np.ndarray) -> np.ndarray:
    """
    Rotate an image 90 degrees counterclockwise.

    Args:
        image: Input image as numpy array

    Returns:
        numpy.ndarray: Rotated image
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("Image must be a numpy array")

    # For 90 degree counterclockwise rotation:
    # New width = old height, New height = old width
    # New pixel at (x, y) comes from old pixel at (y, width-1-x)
    height, width = image.shape[:2]

    if len(image.shape) == 3:
        # Color image with channels
        channels = image.shape[2]
        rotated = np.zeros((width, height, channels), dtype=image.dtype)

        for y in range(height):
            for x in range(width):
                # 90 degree counterclockwise: (x, y) -> (y, width-1-x)
                rotated[width-1-x, y] = image[y, x]
    else:
        # Grayscale image
        rotated = np.zeros((width, height), dtype=image.dtype)

        for y in range(height):
            for x in range(width):
                rotated[width-1-x, y] = image[y, x]

    return rotated


def main():
    try:
        # Load the original image
        image = ft_load("animal.jpeg")
        if image is None:
            print("Failed to load image.")
            return

        print(f"The shape of image is: {image.shape}")
        print(image)

        # Apply zoom from ex03
        zoomed = zoom(image)
        print(f"New shape after slicing: {zoomed.shape} or {zoomed.shape[:2]}")
        print(zoomed)

        # Rotate the zoomed image 90 degrees counterclockwise
        rotated = rotate_90_ccw(zoomed)
        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)

        # Display the rotated image
        if len(rotated.shape) == 3:
            # Remove the single channel dimension for display
            plt.imshow(rotated[:, :, 0], cmap='gray', vmin=0, vmax=255)
        else:
            plt.imshow(rotated, cmap='gray', vmin=0, vmax=255)

        plt.xticks(np.arange(0, rotated.shape[1] + 1, 50))
        plt.yticks(np.arange(0, rotated.shape[0] + 1, 50))
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.title("Rotated Image")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
