# pylint: disable=logging-fstring-interpolation
"Test wrapper"
from typing import Dict, Any
import argparse
import logging
import json
from .sub_namespace_1.submodule1 import validator


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d [%(levelname)-5s] [%(name)-12s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logs = logging.getLogger()


def get_args() -> argparse.Namespace:
    """CLI input parameters."""
    parser = argparse.ArgumentParser(description="test package")
    required_either = parser.add_mutually_exclusive_group(required=True)
    required_either.add_argument(
        "-s", "--schema", help="Path to schema file.", type=str, default=None
    )
    required_either.add_argument(
        "-o", "--object", help="Path to object to validate.", type=str, default=None
    )
    args = parser.parse_args()
    return args


class ReadError(Exception):
    "Object reading error."


def _read(path: str) -> Dict[str, Any]:
    """Function to read the object from json file.

    Args:
        path: Path to object to read.

    Returns:
        Deserialized object.

    Raises:
        ReadError: Raised when json reading/deserialization error occured.
    """
    try:
        with open(path, "r") as fread:
            return json.load(fread)
    except (IOError, FileNotFoundError, FileExistsError, json.JSONDecodeError) as ex:
        raise ReadError from ex


def to_validate() -> None:
    "Validator wrapper."
    args = get_args()

    path_schema = args.schema
    path_obj = args.object

    try:
        schema = _read(path_schema)
    except ReadError as ex:
        logging.error(f"Schema '{path_schema}' reading error: {ex}.")

    try:
        obj = _read(path_obj)
    except ReadError as ex:
        logging.error(f"Object '{path_obj}' reading error: {ex}.")

    flag_str = "valid" if validator(schema, obj) else "not valid"
    logging.info(f"Schema is {flag_str}")
