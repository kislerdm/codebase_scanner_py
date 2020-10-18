#!/usr/bin/env python3
"Program to scan python codebase cross dependecies"

import os
import sys
import logging


class PythonVerionError(Exception):
    "Exception for wrong python version"


def version_check():
    """Function to check python version.

    Raises:
        PythonVerionError: Raised when wrong python version is used.
    """
    ver_major, ver_minor, *_ = sys.version_info
    if ver_major < 3 and ver_minor < 7:
        raise PythonVerionError("Please use python 3.7 and above.")


def main() -> None:
    version_check()
    pass


if __name__ == "__main__":
    main()