"Test setup"
from pathlib import Path
from setuptools import setup, find_namespace_packages  # type: ignore


requirements = (Path(__file__).parent / "requirements.txt").read_text()

setup(
    name="pkg",
    version="1.0",
    license="MIT",
    author="Dmitry Kisler",
    author_email="admin@dkisler.com",
    classifiers=[
        "Development Status :: 2 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    packages=find_namespace_packages(where="."),
    entry_points={
        "console_scripts": [
            "validate = pkg.__main__:to_validate",
        ]
    },
)
