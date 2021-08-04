from datetime import datetime

from telebot.db import SQL


class Update:
    _name = "tlg_update"
    table = f"""
    CREATE TABLE IF NOT EXISTS "{_name}"
    (
        "update_id" INTEGER PRIMARY KEY,
        "created_at" TEXT
    );
    """

    def __init__(self, db: SQL):
        self.db = db

    def print_table(self):
        """ Solo para debug"""
        print(self.table)

    def add(self, update_id):
        """ Agrega un chat 
        Para eso necesita el cursor, inserta los datos
        hace el commit y cierra el cursor.
        """
        now = datetime.now()
        _insert = f"INSERT INTO {self._name}(update_id, created_at) VALUES(?, ?)"
        cur = self.db.cursor()
        cur.execute(_insert, [update_id, now.isoformat()])
        self.db.commit()
        cur.close()


class Message:

    _name = "message"
    table = f"""
    CREATE TABLE IF NOT EXISTS "{_name}"
    (
        "chat_id" INTEGER,
        "msg_id" INTEGER,
        "text" TEXT,
        "created_at" TEXT,
        UNIQUE(chat_id, msg_id) ON CONFLICT REPLACE
        );
    """

    def __init__(self, db: SQL):
        self.db = db

    def print_table(self):
        """ Solo para debug"""
        print(self.table)

    def add(self, chat_id, msg_id, text):
        """ Agrega un chat 
        Para eso necesita el cursor, inserta los datos
        hace el commit y cierra el cursor.
        """
        now = datetime.now()
        now.isoformat()
        _insert = f"""INSERT INTO {self._name}(chat_id, msg_id, text, created_at)
        VALUES(?, ?, ?, ?)"""
        cur = self.db.cursor()
        cur.execute(_insert, [chat_id, msg_id, text, now])
        self.db.commit()
        cur.close()

    def last_message_from(self, chat_id):
        """ en base un chat_id obtiene el ultimo mensaje 
        leido de ese chat """

        _select = f"""select * from {self._name} where chat_id = {chat_id} order by msg_id"""
        row = self.db.one(_select)
        return row
