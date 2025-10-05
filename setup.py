from setuptools import find_packages, setup

setup(
    name="cutstitch",
    version="0.1.0",
    author="rotgruengelb",
    author_email="daniel+cutstitch@rotgruengelb.net",
    description="A tool to stitch images together using various cutout modes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rotgruengelb/cutstitch",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pillow>=11.3.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "cutstitch=cutstitch.cli:main"
        ]
    },
    keywords=["image", "stitch", "cutout", "cli", "tool"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Artistic Software",
        "Topic :: Multimedia :: Graphics"
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
    ],
    project_urls={
        "Homepage": "https://github.com/rotgruengelb/cutstitch",
        "Documentation": "https://github.com/rotgruengelb/cutstitch#readme",
        "Source": "https://github.com/rotgruengelb/cutstitch",
        "Tracker": "https://github.com/rotgruengelb/cutstitch/issues",
    },
)