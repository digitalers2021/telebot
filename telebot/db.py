import sqlite3
from typing import List


class SQL:
    """SQL es un wrapper para sqlite
    Abstrae alguans simples operaciones
    como la creacion de tablas y commits.
    """

    def __init__(self, dbfile: str):
        self.conn = sqlite3.connect(dbfile)

    def setup_db(self, tables: List[str]):
        """ 
        Recive una lista de strings con DDL 
        para la creacion de cada una de
        las tablas.
        """
        cur = self.conn.cursor()
        for t in tables:
            cur.execute(t)
        cur.close()

    def one(self, select_statement: str):
        _select = f"{select_statement} LIMIT 1"
        cur = self.cursor()
        cur.execute(_select)
        row = cur.fetchone()
        cur.close()
        return row

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        """ Thin wrapper for sqlite commit
        """
        self.conn.commit()

    def close(self):
        self.conn.close()
