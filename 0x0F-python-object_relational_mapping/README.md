# 0x0F. Python - Object Relational Mapping

## Description

In this project, we explore the integration of Python with SQL databases using Object Relational Mappers (ORMs). Specifically, we focus on how to connect to a MySQL database, execute SQL queries, and use SQLAlchemy as an ORM to abstract the database interactions.

## Project Setup

### Prerequisites

Ensure you have the following installed:
- Python 3
- MySQL server
- `mysqlclient` and `SQLAlchemy` Python libraries

### Installation Steps

1. **Set up MySQL server**:
    - Install and start MySQL server.
    - Create a database for the project.

2. **Create and activate a Python virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install required Python packages**:
    ```sh
    pip install mysqlclient SQLAlchemy
    ```

## How to Use

### Connecting to MySQL Database

Use the `MySQLdb` module to connect to your MySQL database:
```python
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="your_username",
    passwd="your_password",
    db="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
```
