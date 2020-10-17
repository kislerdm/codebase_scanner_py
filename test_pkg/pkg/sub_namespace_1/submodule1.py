"Submodule with functions"

from typing import Dict, Any
from fastjsonschema import (  # type: ignore
    validate,
    JsonSchemaException,
    JsonSchemaDefinitionException,
)


def validator(schema: Dict[str, Any], obj: Dict[str, Any]) -> bool:
    """Function to validate object against a jsonschema.

    Args:
        schema: Jsonschema.
        obj: Object to validate.

    Returns:
        Flag showing if the object is valid.
    """
    try:
        validate(schema, obj)
        return True
    except (JsonSchemaException, JsonSchemaDefinitionException):
        return False
