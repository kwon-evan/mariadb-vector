import struct

from sqlalchemy.dialects.mysql.base import ischema_names
from sqlalchemy.sql.expression import func
from sqlalchemy.types import UserDefinedType


class VECTOR(UserDefinedType):
    """
    User Defined Type for MariaDB Vector type.
    """

    cache_ok = True

    def __init__(self, size: int):
        super(UserDefinedType, self).__init__()
        if size <= 0 or not isinstance(size, int):
            raise ValueError("Vector size must be a positive integer.")
        self.size = size

    def get_col_spec(self, **kw):
        if self.size is None:
            return "VECTOR"
        return "VECTOR(%d)" % self.size

    def bind_processor(self, dialect):
        def process(value):
            return str(value)

        return process

    def bind_expression(self, bindvalue):
        return func.Vec_FromText(bindvalue)

    def result_processor(self, dialect, coltype):
        def process(value):
            if isinstance(value, bytes):
                num_floats = len(value) // 4
                float_values = struct.unpack(f"{num_floats}f", value)
                return list(float_values)

        return process

    def __repr__(self):
        return f"Vector({self.size})"


# for reflection
ischema_names["vector"] = VECTOR
