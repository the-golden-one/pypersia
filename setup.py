from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pypersia",
    version="1.0.0",
    description="A Python library for Persian utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["pypersia"],
)
