import json
from typing import Sequence
from sqlalchemy.sql.expression import func, Function


def vec_from_seq(array: Sequence) -> Function:
    """
    Converts a Python list or NumPy array to a MariaDB-compatible vector function.

    Args:
        array (Sequence): Input array to be converted.

    Returns:
        sqlalchemy.sql.expression.Function: SQL function for Vec_FromText.
    """
    if not isinstance(array, Sequence):
        raise TypeError("Input array must be a sequence.")

    return func.Vec_FromText(json.dumps(array))
