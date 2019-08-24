"""A setuptools based setup module.
"""

from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "gerardo", "__version__.py")) as f:
    version = f.read().split('"')[1]

setup(
    name="gerardo",
    version=version,
    description="Simple decorator for multiprocessing and psql insertion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinywlui/gerardo",
    author="kevin lui",
    author_email="kevinywlui@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="psql multiprocessing",
    packages=["gerardo"],
    install_requires=["psycopg2-binary"],
)
