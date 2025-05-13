# MariaDB Vector
Integrate MariaDB's VECTOR type with SQL Alchemy and SQL Model

## Installation
```bash
pip install mariadb-vector
```

## Usage

### Add a vector column
```python
from sqlmodel import SQLModel, Field, Column
from mariadb_vector import Vector


class Item(SQLModel, table=True):
    embedding: list[float] = Field(sa_column=Column(Vector(3)))
```

### Insert a vector
```python
item = Item(embedding=[0.1, 0.2, 0.3])
session.add(item)
session.commit()
```

### Vector Search
The following functions are available for calculating vector distances:

`vec_from_seq(array: Sequence)`
- Converts a Python list or NumPy array into a database-compatible vector function.

`vec_distance(v1, v2)`
- Calculates a general distance between two vectors.

`vec_distance_euclidean(v1, v2)`
- Calculates the Euclidean distance between two vectors.

`vec_distance_cosine(v1, v2)`
- Calculates the cosine distance between two vectors.

```python
# Assume `engine` is already created and connected to your database.
with Session(engine) as session:
    target_vector = [0.1, 0.2, 0.3]
    query = (
        select(Item.id)
        .order_by(vec_distance_euclidean(Item.embedding, target_vector))
        .limit(2)
    )
    result = session.exec(query).all()
    print(result)
```

## Diagram
```mermaid
flowchart TB
    subgraph "User Layer"
        App["User Application (Python code)"]:::python
    end

    subgraph "ORM & Extension Layer"
        ORM["SQLModel / SQLAlchemy"]:::orm
        subgraph "MariaDB-Vector Library"
            LibRoot["MariaDB-Vector Library"]:::library
            LibInit["__init__.py"]:::library
            VecType["Vector Type"]:::library
            VecFuncs["Vector Functions"]:::library
        end
    end

    subgraph "Database Layer"
        DB["MariaDB Database with VECTOR support"]:::db
    end

    subgraph "Build & CI"
        Config1["pyproject.toml"]:::config
        Config2["pdm.lock"]:::config
        WFfmt[".github/workflows/format.yml"]:::config
        WFrelease[".github/workflows/release.yml"]:::config
        Readme["README.md"]:::config
        License["LICENSE"]:::config
    end

    App -->|"imports extension"| LibRoot
    App -->|"executes session operations"| ORM
    LibRoot --> LibInit
    LibRoot --> VecType
    LibRoot --> VecFuncs
    VecType -->|"integrates with ORM"| ORM
    VecFuncs -->|"integrates with ORM"| ORM
    ORM -->|"compiles SQL"| DB
    DB -->|"returns results"| ORM
    ORM -->|"maps to models"| App

    click LibRoot "https://github.com/kwon-evan/mariadb-vector/tree/main/src/mariadb_vector"
    click VecType "https://github.com/kwon-evan/mariadb-vector/blob/main/src/mariadb_vector/vector.py"
    click VecFuncs "https://github.com/kwon-evan/mariadb-vector/blob/main/src/mariadb_vector/functions.py"
    click LibInit "https://github.com/kwon-evan/mariadb-vector/blob/main/src/mariadb_vector/__init__.py"
    click Config1 "https://github.com/kwon-evan/mariadb-vector/blob/main/pyproject.toml"
    click Config2 "https://github.com/kwon-evan/mariadb-vector/blob/main/pdm.lock"
    click WFfmt "https://github.com/kwon-evan/mariadb-vector/blob/main/.github/workflows/format.yml"
    click WFrelease "https://github.com/kwon-evan/mariadb-vector/blob/main/.github/workflows/release.yml"
    click Readme "https://github.com/kwon-evan/mariadb-vector/blob/main/README.md"
    click License "https://github.com/kwon-evan/mariadb-vector/tree/main/LICENSE"

    classDef python fill:#D0E6FB,stroke:#0366D6,color:#0366D6;
    classDef library fill:#E8F4FC,stroke:#1B82D1,color:#1B82D1;
    classDef orm fill:#E6F9E6,stroke:#2C9E2C,color:#2C9E2C;
    classDef db fill:#FFF4E5,stroke:#E69100,color:#E69100;
    classDef config fill:#F0F0F0,stroke:#666666,color:#333333;
```

# Contributing
- This library is inspired by the [pgvector-python](https://github.com/pgvector/pgvector-python) and is built to bring similar functionality to MariaDB.
- Any contributions, bug reports, or improvements are welcome!
- Feel free to open issues or submit pull requests.
