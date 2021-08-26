import sqlite3
from pprint import pprint

from telebot import conf, telegram
from telebot.db import SQL
from telebot.models import Message, Update

options = conf.open_env()
# print(options) # debug
token = options["TELEGRAM_TOKEN"]
db_name = options.get("DBFILE", "telegram.db")
db = SQL(db_name)

db.setup_db([Update.table, Message.table])

def get_updates():
    """ A wrapper que envuelve la funcionalidad
    de obtener updates desde telegram
    """
    """Agregada variable de offset y pasada por parametro en update
    """
    offset = db.one('SELECT update_id FROM tlg_update order by update_id desc')
    updates = telegram.get_updates(token, *offset)
    for _upt in updates:
        update = Update(db)
        try:
            update.add(_upt["update_id"])
            telegram.register_message(db, _upt["message"], token)
        except sqlite3.IntegrityError:
            print("Update ya registrado")

        # pprint(_upt) # debug

get_updates()