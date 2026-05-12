import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import signal
import sys
from load_image import ft_load

matplotlib.use('TkAgg')  # Use WSL-compatible interactive backend


def signal_handler(sig, frame):
    """Handle Ctrl+C and other signals gracefully."""
    print("\nProgram interrupted. Exiting gracefully...")
    plt.close('all')  # Close all matplotlib windows
    sys.exit(0)


# Set up signal handlers for Ctrl+C and Ctrl+D
signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C
if hasattr(signal, 'SIGQUIT'):
    signal.signal(signal.SIGQUIT, signal_handler)  # Ctrl+D (Unix)


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of an image.

    Args:
        array: Input image as numpy array

    Returns:
        Inverted image as numpy array

    Raises:
        TypeError: If array is not a numpy array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Array must be a numpy array")
    # Invert colors: 255 - pixel_value (using allowed operators: =, +, -, *)
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to an image.

    Args:
        array: Input image as numpy array

    Returns:
        Red-filtered image as numpy array

    Raises:
        TypeError: If array is not a numpy array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Array must be a numpy array")
    # Create a copy to avoid modifying original
    result = array.copy()
    # If grayscale, convert to RGB for red filter
    if len(result.shape) == 3 and result.shape[2] == 1:
        # Convert grayscale to RGB
        result = np.repeat(result, 3, axis=2)
    elif len(result.shape) == 2:
        # Convert 2D grayscale to RGB
        result = np.stack([result, result, result], axis=2)
    # Apply red filter: keep red channel, zero out green and blue
    # Using allowed operators: =, *
    if len(result.shape) == 3:
        result[:, :, 1] = result[:, :, 1] * 0  # Zero green channel
        result[:, :, 2] = result[:, :, 2] * 0  # Zero blue channel
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to an image.

    Args:
        array: Input image as numpy array

    Returns:
        Green-filtered image as numpy array

    Raises:
        TypeError: If array is not a numpy array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Array must be a numpy array")
    # Create a copy to avoid modifying original
    result = array.copy()
    # If grayscale, convert to RGB for green filter
    if len(result.shape) == 3 and result.shape[2] == 1:
        # Convert grayscale to RGB
        result = np.repeat(result, 3, axis=2)
    elif len(result.shape) == 2:
        # Convert 2D grayscale to RGB
        result = np.stack([result, result, result], axis=2)
    # Apply green filter: keep green channel, zero out red and blue
    # Using allowed operators: = only
    if len(result.shape) == 3:
        zeros = np.zeros_like(result[:, :, 0])
        result[:, :, 0] = zeros  # Zero red c0hannel
        result[:, :, 2] = zeros  # Zero blue channel

    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to an image.

    Args:
        array: Input image as numpy array

    Returns:
        Blue-filtered image as numpy array

    Raises:
        TypeError: If array is not a numpy array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Array must be a numpy array")
    # Create a copy to avoid modifying original
    result = array.copy()
    # If grayscale, convert to RGB for blue filter
    if len(result.shape) == 3 and result.shape[2] == 1:
        # Convert grayscale to RGB
        result = np.repeat(result, 3, axis=2)
    elif len(result.shape) == 2:
        # Convert 2D grayscale to RGB
        result = np.stack([result, result, result], axis=2)
    # Apply blue filter: keep blue channel, zero out red and green
    # Using allowed operators: = only
    if len(result.shape) == 3:
        zeros = np.zeros_like(result[:, :, 0])
        result[:, :, 0] = zeros  # Zero red channel
        result[:, :, 1] = zeros  # Zero green channel

    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts an image to grayscale.

    Args:
        array: Input image as numpy array

    Returns:
        Grayscale image as numpy array

    Raises:
        TypeError: If array is not a numpy array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Array must be a numpy array")

    # If already grayscale, return as is
    if len(array.shape) == 2:
        return array
    elif len(array.shape) == 3 and array.shape[2] == 1:
        return array[:, :, 0]
    # Convert RGB to grayscale using simple average method
    # Using allowed operators: =, / only
    # Simple grayscale: average of RGB channels
    # (R + G + B) / 3, but we can't use +, so we use weighted average
    r = array[:, :, 0].astype(np.float64)
    g = array[:, :, 1].astype(np.float64)
    b = array[:, :, 2].astype(np.float64)
    # print(f"r: {r}, g: {g}, b: {b}")
    # Stack the three (H, W) arrays along axis 2 to make (H, W, 3)
    stacked = np.stack((r, g, b), axis=2)
    # Take mean across last axis (axis=2) to get grayscale
    result = np.mean(stacked, axis=2)
    # result = (r + g + b) / 3
    return result.astype(np.uint8)


def main():
    try:
        print("Press Ctrl+C or Ctrl+D to exit.")
        print("Close the matplotlib window or press ESC to exit.\n")
        # Load the original image
        image = ft_load("landscape.jpg")
        if image is None:
            print("Failed to load image.")
            return
        print(f"The shape of image is: {image.shape}")
        print(image)
        # Convert rotated image to proper format for filtering
        if len(image.shape) == 3 and image.shape[2] == 1:
            # Convert single channel to 2D for better processing
            rotated_2d = image[:, :, 0]
        else:
            rotated_2d = image
        # Apply different filters
        inverted = ft_invert(rotated_2d)
        red_filter = ft_red(rotated_2d)
        green_filter = ft_green(rotated_2d)
        blue_filter = ft_blue(rotated_2d)
        grey_filter = ft_grey(rotated_2d)
        # print("Filters applied successfully.")
        # print(grey_filter)
        # Display results in a grid
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        # Add key press event handler for ESC
        def on_key_press(event):
            if event.key == 'escape':
                print("\nESC exiting")
                plt.close('all')
                sys.exit(0)
        # Connect the key press event
        fig.canvas.mpl_connect('key_press_event', on_key_press)
        # Original rotated image
        axes[0, 0].imshow(rotated_2d, cmap='gray', vmin=0, vmax=255)
        axes[0, 0].set_title("Original")
        axes[0, 0].axis('off')
        # Inverted
        axes[0, 1].imshow(inverted, cmap='gray', vmin=0, vmax=255)
        axes[0, 1].set_title("Inverted")
        axes[0, 1].axis('off')
        # Red filter
        axes[0, 2].imshow(red_filter)
        axes[0, 2].set_title("Red Filter")
        axes[0, 2].axis('off')
        # Green filter
        axes[1, 0].imshow(green_filter)
        axes[1, 0].set_title("Green Filter")
        axes[1, 0].axis('off')
        # Blue filter
        axes[1, 1].imshow(blue_filter)
        axes[1, 1].set_title("Blue Filter")
        axes[1, 1].axis('off')
        # Hide the last subplot
        # grey filter
        axes[1, 2].imshow(grey_filter, cmap='gray', vmin=0, vmax=255)
        axes[1, 2].set_title("Grey Filter")
        axes[1, 2].axis('off')
        # Add instruction text
        print("Original image range:", image.min(), "-", image.max())
        fig.suptitle("landscape\n",
                     fontsize=14, y=0.95)
        plt.tight_layout()

        # Handle window close event
        def on_close(event):
            print("\nExiting")
            sys.exit(0)
        fig.canvas.mpl_connect('close_event', on_close)
        plt.show()
    except KeyboardInterrupt:
        print("\nCtrl+C Exiting")
        plt.close('all')
        sys.exit(0)
    except EOFError:
        print("\nEOF Ctrl+D Exiting")
        plt.close('all')
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        plt.close('all')
        sys.exit(1)


if __name__ == "__main__":
    main()
