import hashlib
from pathlib import Path
from PIL import Image


def compute_image_hash(image_path: Path) -> str:
    """
    Compute SHA256 hash of the image's raw RGBA bytes.
    Ensures consistency regardless of metadata.
    """
    with Image.open(image_path).convert("RGBA") as img:
        data = img.tobytes()
    return hashlib.sha256(data).hexdigest()
