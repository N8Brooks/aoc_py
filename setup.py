import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="aoc",  # Replace with your own username
    version="0.0.1",
    author="Nathan Brooks",
    author_email="natebrooks004@gmail.com",
    description="Advent of Code Solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/N8Brooks/aoc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=["numpy>=1.19.2", "more_itertools>=8.6.0"],
)
