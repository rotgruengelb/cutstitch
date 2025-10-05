import os
from pathlib import Path

from cutstitch import stitch_images
from .utils import compute_image_hash, open_images

ASSETS = Path(__file__).parent / "assets"
OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

EXPECTED_HASHES = {"vertical.png": "<fill-in-later>",
                   "diagonal45.png": "<fill-in-later>",
                   "diagonal65.png": "<fill-in-later>",
                   "diagonal77.png": "<fill-in-later>",
                   "diagonal12.png": "<fill-in-later>",
                   "circle.png": "<fill-in-later>"}


def run_stitch_test(tmp_path, output_name, files, mode, **kwargs):
    output = tmp_path / output_name
    stitch_images(open_images(files), mode=mode, **kwargs).save(output)

    assert os.path.exists(output)
    file_hash = compute_image_hash(output)
    expected_hash = EXPECTED_HASHES[output_name]
    if expected_hash != "<fill-in-later>":
        assert file_hash == expected_hash, f"Hash mismatch: {file_hash}"
    else:
        print(f"{output_name[:-4].capitalize()} hash: {file_hash}")


def test_vertical_stitch(tmp_path):
    run_stitch_test(tmp_path, "vertical.png", [ASSETS / "img1.png", ASSETS / "img2.png"], mode="vertical")


def test_diagonal_45_stitch(tmp_path):
    run_stitch_test(tmp_path, "diagonal45.png", [ASSETS / "img1.png", ASSETS / "img2.png", ASSETS / "img3.png"],
        mode="diagonal")


def test_diagonal_65_stitch(tmp_path):
    run_stitch_test(tmp_path, "diagonal65.png", [ASSETS / "img1.png", ASSETS / "img2.png", ASSETS / "img3.png"],
        mode="diagonal", angle=65)


def test_diagonal_77_stitch(tmp_path):
    run_stitch_test(tmp_path, "diagonal77.png", [ASSETS / "img1.png", ASSETS / "img2.png", ASSETS / "img3.png"],
        mode="diagonal", angle=77)


def test_diagonal_12_stitch(tmp_path):
    run_stitch_test(tmp_path, "diagonal12.png", [ASSETS / "img1.png", ASSETS / "img2.png", ASSETS / "img3.png"],
        mode="diagonal", angle=12)


def test_circle_stitch(tmp_path):
    run_stitch_test(tmp_path, "circle.png", [ASSETS / "img1.png", ASSETS / "img2.png", ASSETS / "img3.png"],
        mode="circle")
