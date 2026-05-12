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


def main():
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            print("Failed to load image.")
            return

        # Print original image info
        print(f"The shape of image is: {image.shape}")
        print(image)

        # Zoom and convert
        zoomed = zoom(image)
        print(f"New shape after slicing: {zoomed.shape} or {zoomed.shape[:2]}")
        print(zoomed)

        # Display the grayscale zoomed image
        plt.imshow(zoomed[:, :, 0], cmap='gray', vmin=0, vmax=255)
        plt.xticks(np.arange(0, 401, 50))
        plt.yticks(np.arange(0, 401, 50))
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.title("Zoomed Grayscale Image")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
