from PIL import Image, ImageDraw
from .modes import CUTOUT_MODES


def create_cutout_mask(image_size, image_index, total_images, mode, **kwargs):
    """Create a mask for one image using the specified cutout mode."""
    mask = Image.new("L", image_size, 0)
    draw = ImageDraw.Draw(mask)

    if mode not in CUTOUT_MODES:
        raise ValueError(f"Unknown cutout mode: {mode}")

    CUTOUT_MODES[mode](draw, image_size, image_index, total_images, **kwargs)
    return mask


def stitch_images(image_files, mode="vertical", output_file="stitched.png", **kwargs):
    opened_images = [Image.open(file).convert("RGBA") for file in image_files]

    base_width, base_height = opened_images[0].size
    for i in range(1, len(opened_images)):
        if opened_images[i].size != (base_width, base_height):
            opened_images[i] = opened_images[i].resize((base_width, base_height))

    stitched_result = Image.new("RGBA", (base_width, base_height))

    for image_index, image in enumerate(opened_images):
        mask = create_cutout_mask(
            (base_width, base_height),
            image_index,
            len(opened_images),
            mode,
            **kwargs
        )
        stitched_result.paste(image, (0, 0), mask)

    stitched_result.save(output_file)
    return output_file
