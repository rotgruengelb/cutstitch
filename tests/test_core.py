import os
from pathlib import Path
from cutstitch.core import stitch_images
from utils import compute_image_hash

ASSETS = Path(__file__).parent / "assets"
OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Expected reference hashes (fill in later)
EXPECTED_HASHES = {
    "vertical.png": "<fill-in-later>",
    "diagonal.png": "<fill-in-later>",
    "circle.png": "<fill-in-later>",
}

def test_vertical_stitch(tmp_path):
    output = tmp_path / "vertical.png"
    files = [ASSETS / "img1.png", ASSETS / "img2.png"]
    stitched = stitch_images(files, mode="vertical", output_file=output)

    assert os.path.exists(stitched)
    file_hash = compute_image_hash(output)
    if EXPECTED_HASHES["vertical.png"] != "<fill-in-later>":
        assert file_hash == EXPECTED_HASHES["vertical.png"], f"Hash mismatch: {file_hash}"
    else:
        print(f"Vertical hash: {file_hash}")


def test_diagonal_stitch(tmp_path):
    output = tmp_path / "diagonal.png"
    files = [ASSETS / "img1.png", ASSETS / "img2.png", ASSETS / "img3.png"]
    stitched = stitch_images(files, mode="diagonal", angle=45, output_file=output)

    assert os.path.exists(stitched)
    file_hash = compute_image_hash(output)
    if EXPECTED_HASHES["diagonal.png"] != "<fill-in-later>":
        assert file_hash == EXPECTED_HASHES["diagonal.png"], f"Hash mismatch: {file_hash}"
    else:
        print(f"Diagonal hash: {file_hash}")


def test_circle_stitch(tmp_path):
    output = tmp_path / "circle.png"
    files = [ASSETS / "img1.png", ASSETS / "img2.png", ASSETS / "img3.png"]
    stitched = stitch_images(files, mode="circle", output_file=output)

    assert os.path.exists(stitched)
    file_hash = compute_image_hash(output)
    if EXPECTED_HASHES["circle.png"] != "<fill-in-later>":
        assert file_hash == EXPECTED_HASHES["circle.png"], f"Hash mismatch: {file_hash}"
    else:
        print(f"Circle hash: {file_hash}")
