import json
from typing import Sequence
from sqlalchemy.sql.expression import func, Function
from sqlalchemy.orm.attributes import InstrumentedAttribute


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


def vec_distance(
    v1: Sequence | InstrumentedAttribute,
    v2: Sequence | InstrumentedAttribute,
) -> Function:
    """
    Calculates the distance between two vectors using a general VEC_DISTANCE function.

    This function generates a SQL expression for calculating the distance
    between two vectors in a database column (v1) and a Python sequence (v2).

    Args:
        v1 (InstrumentedAttribute): The first vector, which must be a database column.
        v2 (Sequence): The second vector, which must be a Python sequence.

    Returns:
        sqlalchemy.sql.expression.Function: SQL function for VEC_DISTANCE.

    Raises:
        TypeError: If v1 is not an InstrumentedAttribute or v2 is not a Sequence.
    """
    if not isinstance(v1, InstrumentedAttribute):
        raise TypeError("v1 must be an InstrumentedAttribute.")

    if not isinstance(v2, Sequence):
        raise TypeError("v2 must be a sequence.")

    return func.VEC_DISTANCE(v1, vec_from_seq(v2))


def vec_distance_euclidean(
    v1: Sequence | InstrumentedAttribute,
    v2: Sequence | InstrumentedAttribute,
) -> Function:
    """
    Calculates the Euclidean distance between two vectors.

    This function generates a SQL expression for calculating the Euclidean distance
    between two vectors in a database column (v1) and a Python sequence (v2).

    Args:
        v1 (InstrumentedAttribute): The first vector, which must be a database column.
        v2 (Sequence): The second vector, which must be a Python sequence.

    Returns:
        sqlalchemy.sql.expression.Function: SQL function for VEC_DISTANCE_EUCLIDEAN.

    Raises:
        TypeError: If v1 is not an InstrumentedAttribute or v2 is not a Sequence.
    """
    if not isinstance(v1, InstrumentedAttribute):
        raise TypeError("v1 must be an InstrumentedAttribute.")

    if not isinstance(v2, Sequence):
        raise TypeError("v2 must be a sequence.")

    return func.VEC_DISTANCE_EUCLIDEAN(v1, vec_from_seq(v2))


def vec_distance_cosine(
    v1: Sequence | InstrumentedAttribute,
    v2: Sequence | InstrumentedAttribute,
) -> Function:
    """
    Calculates the cosine distance between two vectors.

    This function generates a SQL expression for calculating the cosine distance
    between two vectors in a database column (v1) and a Python sequence (v2).

    Args:
        v1 (InstrumentedAttribute): The first vector, which must be a database column.
        v2 (Sequence): The second vector, which must be a Python sequence.

    Returns:
        sqlalchemy.sql.expression.Function: SQL function for VEC_DISTANCE_COSINE.

    Raises:
        TypeError: If v1 is not an InstrumentedAttribute or v2 is not a Sequence.
    """
    if not isinstance(v1, InstrumentedAttribute):
        raise TypeError("v1 must be an InstrumentedAttribute.")

    if not isinstance(v2, Sequence):
        raise TypeError("v2 must be a sequence.")

    return func.VEC_DISTANCE_COSINE(v1, vec_from_seq(v2))
