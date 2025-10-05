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


def cutout_diagonal(draw, image_size, image_index, total_images, angle=45, **kwargs):
    width, height = image_size
    band_width = width / total_images

    left = image_index * band_width
    right = (image_index + 1) * band_width
    rect = [(left, 0), (right, 0), (right, height), (left, height)]

    offset = math.tan(math.radians(angle)) * width
    polygon_points = [
        (left, -offset),
        (right, 0),
        (right, height + offset),
        (left, height),
    ]

    draw.polygon(polygon_points, fill=255)


def cutout_circle(draw, image_size, image_index, total_images, **kwargs):
    width, height = image_size
    min_dimension = min(width, height)
    max_radius = min_dimension / 2

    # Radius for each "ring" boundary
    radius_step = max_radius / total_images
    center_x, center_y = width / 2, height / 2

    # The outer and inner radius for this ring
    outer_radius = max_radius - image_index * radius_step
    inner_radius = outer_radius - radius_step

    # Outer circle (white)
    outer_box = [
        center_x - outer_radius, center_y - outer_radius,
        center_x + outer_radius, center_y + outer_radius,
    ]
    draw.ellipse(outer_box, fill=255)

    # Inner circle (cut out the hole), except for the last one
    if image_index < total_images - 1:
        inner_box = [
            center_x - inner_radius, center_y - inner_radius,
            center_x + inner_radius, center_y + inner_radius,
        ]
        draw.ellipse(inner_box, fill=0)


CUTOUT_MODES = {
    "vertical": cutout_vertical,
    "horizontal": cutout_horizontal,
    "diagonal": cutout_diagonal,
    "circle": cutout_circle,
}
