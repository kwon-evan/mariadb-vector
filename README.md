# MariaDB Vector
Integrate MariaDB's VECTOR type with SQL Alchemy and SQL Model

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
## Contributing
- This library is inspired by the [pgvector-python](https://github.com/pgvector/pgvector-python) and is built to bring similar functionality to MariaDB.  
- Any contributions, bug reports, or improvements are welcome!  
- Feel free to open issues or submit pull requests.
