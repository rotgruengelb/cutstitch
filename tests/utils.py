import hashlib
from pathlib import Path
from typing import List

from PIL import Image


def compute_image_hash(image_path: Path) -> str:
    with Image.open(image_path).convert("RGBA") as img:
        data = img.tobytes()
    return hashlib.sha256(data).hexdigest()


def open_images(image_paths: List[Path]) -> List[Image.Image]:
    return [Image.open(path).convert("RGBA") for path in image_paths]