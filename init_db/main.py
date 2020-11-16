"""fill the database with initial data"""

import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


user = "postgres"  # postgres default
with open(os.environ["POSTGRES_PASSWORD_FILE"], "r") as f:
    password = f.read().strip()


engine = create_engine(f"postgresql+psycopg2://{user}:{password}@db/{user}", echo=True)
meta = MetaData()

parts = Table(
    "parts",
    meta,
    Column("id", Integer, primary_key=True),
    Column("manufacturer", String),
    Column("mpn", String),
    Column("description", String),
    Column("note", String),
)

meta.create_all(engine)  # OK if exists
