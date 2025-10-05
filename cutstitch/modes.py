import math
from enum import Enum

from PIL import ImageDraw

Dimensions = tuple[int, int]


def cutout_vertical(draw: ImageDraw.ImageDraw, image_size: Dimensions, stripe_index: int, num_stripes: int, **kwargs):
    """
    Draws a vertical stripe mask on the given draw object.

    Args:
        draw (ImageDraw.ImageDraw): The mask drawing object.
        image_size (tuple[int, int]): (width, height) of the image.
        stripe_index (int): The index of the stripe to draw.
        num_stripes (int): The total number of vertical stripes.
    """
    width, height = image_size
    stripe_width = width // num_stripes
    left = stripe_index * stripe_width
    right = (stripe_index + 1) * stripe_width

    draw.rectangle([left, 0, right, height], fill=255)


def cutout_horizontal(draw: ImageDraw.ImageDraw, image_size: Dimensions, stripe_index: int, num_stripes: int, **kwargs):
    """
    Draws a horizontal stripe mask on the given draw object.

    Args:
        draw (ImageDraw.ImageDraw): The mask drawing object.
        image_size (tuple[int, int]): (width, height) of the image.
        stripe_index (int): The index of the stripe to draw.
        num_stripes (int): The total number of horizontal stripes.
    """
    width, height = image_size
    stripe_height = height // num_stripes
    top = stripe_index * stripe_height
    bottom = (stripe_index + 1) * stripe_height

    draw.rectangle([0, top, width, bottom], fill=255)


def cutout_diagonal(draw: ImageDraw.ImageDraw, image_size: Dimensions, band_index: int, num_bands: int,
                    angle: float = 45, **kwargs):
    """
    Draws a diagonal band mask on the given draw object.

    Args:
        draw (ImageDraw.ImageDraw): The mask drawing object.
        image_size (tuple[int, int]): (width, height) of the image.
        band_index (int): The index of the diagonal band to draw.
        num_bands (int): The total number of diagonal bands.
        angle (float): The angle of the diagonal in degrees (default: 45).
    """
    width, height = image_size
    radians = math.radians(angle)
    diag_length = abs(width * math.cos(radians)) + abs(height * math.sin(radians))
    band_width = diag_length / num_bands
    band_start = band_index * band_width
    band_end = (band_index + 1) * band_width

    for y in range(height):
        x_start = int((band_start - y * math.sin(radians)) / math.cos(radians))
        x_end = int((band_end - y * math.sin(radians)) / math.cos(radians))
        x0 = max(0, min(width, x_start))
        x1 = max(0, min(width, x_end))
        if x0 != x1:
            draw.line([(x0, y), (x1, y)], fill=255)


def cutout_circle(draw: ImageDraw.ImageDraw, image_size: Dimensions, ring_index: int, num_rings: int, **kwargs):
    """
    Draws a circular ring mask on the given draw object.

    Args:
        draw (ImageDraw.ImageDraw): The mask drawing object.
        image_size (tuple[int, int]): (width, height) of the image.
        ring_index (int): The index of the ring to draw.
        num_rings (int): The total number of concentric rings.
        **kwargs: Additional arguments (unused).
    """
    width, height = image_size
    center_x, center_y = width // 2, height // 2
    max_radius = min(width, height) // 2
    ring_width = max_radius / num_rings
    inner_radius = int(ring_index * ring_width)
    outer_radius = int((ring_index + 1) * ring_width)

    draw.ellipse([center_x - outer_radius, center_y - outer_radius, center_x + outer_radius, center_y + outer_radius],
                 fill=255)

    if inner_radius > 0:
        draw.ellipse(
            [center_x - inner_radius, center_y - inner_radius, center_x + inner_radius, center_y + inner_radius],
            fill=0)


CUTOUT_MODES = {"vertical": cutout_vertical,
                "horizontal": cutout_horizontal,
                "diagonal": cutout_diagonal,
                "circle": cutout_circle}

