# MariaDB Vector
SQL Alchemy, SQL Model and MariaDB's VECTOR type integration with MariaDB

## Installation
```bash
pdm add git+https://github.com/kwon-evan/sqlalchemy-mariadb-vector.git
# or
pip install git+https://github.com/kwon-evan/sqlalchemy-mariadb-vector.git
```

## Usage
### SQL Model

Add a vector column
```python
from sqlmodel import SQLModel, Field, Column
from mariadb_vector import Vector


class Item(SQLModel, table=True):
    embedding: list[float] = Field(sa_column=Column(Vector(3)))
```

Insert a vector
```python
item = Item(embedding=[0.1, 0.2, 0.3])
session.add(item)
session.commit()
```

