import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from model.payload import Payload


class Postgres:
    TABLE_NAME = "parts"

    def __init__(self):
        user = "postgres"
        with open(os.environ["POSTGRES_PASSWORD_FILE"], "r") as f:
            password = f.read().strip()

        self.engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@db/{user}", echo=True
        )
        self.meta = MetaData()

    @property
    def table(self):
        return Table(
            self.TABLE_NAME,
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("manufacturer", String),
            Column("mpn", String),
            Column("description", String),
            Column("note", String),
        )

    def create_table(self):
        self.meta.create_all(self.engine)

    def select(self, payload: Payload):
        payload_tuple = (payload.part_id, payload.manufacturer, payload.mpn)
        lookup = ("part_id", "manufacturer", "mpn")
        if payload_tuple is (None, None, None):
            where_clause = ""
        elif payload_tuple is (payload.part_id, None, None):
            where_clause = f"WHERE part_id={payload.part_id}"
        elif payload_tuple is (None, payload.manufacturer, None):
            where_clause = f"WHERE manufacturer={payload.manufacturer}"
        elif payload_tuple is (payload.mpn, None, None):
            where_clause = f"WHERE mpn={payload.mpn}"
        else:
            where_clause = "WHERE ("
            for i, value in enumerate(payload_tuple):
                if value is None:
                    pass
                where_clause += f"{lookup[i]}={value} AND"
            where_clause = where_clause[:-4] + ")"

        query_result = self.engine.execute(
            f"SELECT * FROM {self.TABLE_NAME}{where_clause}"
        )
        return query_result
