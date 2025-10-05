import math


def cutout_vertical(draw, image_size, image_index, total_images, **kwargs):
    width, height = image_size
    stripe_width = width / total_images
    left = int(image_index * stripe_width)
    right = int((image_index + 1) * stripe_width)
    draw.rectangle([left, 0, right, height], fill=255)


def cutout_horizontal(draw, image_size, image_index, total_images, **kwargs):
    width, height = image_size
    stripe_height = height / total_images
    top = int(image_index * stripe_height)
    bottom = int((image_index + 1) * stripe_height)
    draw.rectangle([0, top, width, bottom], fill=255)


CUTOUT_MODES = {
    "vertical": cutout_vertical,
    "horizontal": cutout_horizontal,
}
