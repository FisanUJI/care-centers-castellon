import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_images(image_paths):
    """
    Display images in a grid layout with captions.
    Args:
        image_paths (list of tuples): List of (image_path, caption) tuples.
    """
    num_images = len(image_paths)
    fig, axes = plt.subplots(1, num_images, figsize=(15, 5))
    for ax, (path, caption) in zip(axes, image_paths):
        img = mpimg.imread(path)
        ax.imshow(img)
        ax.axis('off')
        ax.set_title(caption)
    plt.show()