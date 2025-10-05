import argparse
import random

from PIL import Image

from .core import stitch_images
from .modes import CUTOUT_MODES


def main():
    parser = argparse.ArgumentParser(description="Stitch images with configurable cutouts.")
    parser.add_argument("files", nargs="+", help="image files to stitch together (two or more, in order)")
    parser.add_argument("--mode", choices=list(CUTOUT_MODES.keys()), default="vertical", help="cutout mode (default: vertical)")
    parser.add_argument("--angle", type=float, default=45, help="angle for diagonal mode")
    parser.add_argument("--output", default="stitched.png", help="output file name")
    parser.add_argument("--shuffle-files", type=bool, default=False, help="randomly shuffle input files before stitching")
    args = parser.parse_args()

    if len(args.files) < 2:
        raise RuntimeError("Must provide at least two image files")

    images = [Image.open(path).convert("RGBA") for path in args.files]
    if args.shuffle_files:
        random.shuffle(images)
    stitch_images(images, args.mode, angle=args.angle).save(args.output)
    print(f"Saved stitched image to {args.output}")


if __name__ == "__main__":
    main()
