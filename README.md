# cutstitch

A tool to stitch images together using various cutout modes.

## Usage

### CLI

```
usage: cutstitch [-h] [--mode {vertical,horizontal,diagonal,circle}] [--angle ANGLE] [--output OUTPUT] files [files ...]

positional arguments:
  files                 Image files to stitch together (two or more, in order)

options:
  -h, --help            show this help message and exit
  --mode {vertical,horizontal,diagonal,circle}
                        Cutout mode (default: vertical)
  --angle ANGLE         Angle for diagonal mode
  --output OUTPUT       Output file name
```

#### Examples
```sh
cutstitch image1.png image2.png --mode vertical --output result.png
```

## Features
- Stitch multiple images together
- Multiple  cutout modes
- Simple CLI
