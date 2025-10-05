from typing import List, Tuple, Any

from PIL import ImageDraw, Image

from .modes import CUTOUT_MODES


def create_cutout_mask(image_size: Tuple[int, int], image_index: int, total_images: int, mode: str,
                       **kwargs: Any) -> Image.Image:
    """
    Creates a mask for cutting out a specific region of an image based on the given mode.

    Args:
        image_size (Tuple[int, int]): The (width, height) of the mask.
        image_index (int): The index of the current region/image.
        total_images (int): The total number of regions/images.
        mode (str): The cutout mode.
        **kwargs: Additional mode-specific parameters.

    Returns:
        Image.Image: The cutout mask in mode "L" (grayscale).

    Raises:
        ValueError: If an unknown cutout mode is provided.
    """
    mask = Image.new("L", image_size, 0)
    draw = ImageDraw.Draw(mask)

    if mode not in CUTOUT_MODES:
        raise ValueError(f"Unknown cutout mode: {mode}")

    CUTOUT_MODES[mode](draw, image_size, image_index, total_images, **kwargs)
    return mask


def stitch_images(images: List[Image.Image], mode: str = "vertical", **kwargs: Any) -> Image.Image:
    """
    Stitches multiple images together using cutout masks, combining them into one output image.

    Args:#
        images (List[Image.Image]): The images to stitch.
        mode (str, optional): Cutout mode for stitching. (default: "vertical")
        **kwargs: Additional cutout mode-specific parameters.

    Returns:
        Image.Image: The stitched image.
    """

    base_width, base_height = images[0].size
    for i in range(1, len(images)):
        if images[i].size != (base_width, base_height):
            images[i] = images[i].resize((base_width, base_height))

    stitched_result = Image.new("RGBA", (base_width, base_height))

    for image_index, image in enumerate(images):
        mask = create_cutout_mask((base_width, base_height), image_index, len(images), mode, **kwargs)
        stitched_result.paste(image, (0, 0), mask)

    return stitched_result
