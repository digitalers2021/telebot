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


def get_updates():
    """ A wrapper que envuelve la funcionalidad
    de obtener updates desde telegram
    """
    updates = telegram.get_updates(token)
    for _upt in updates:
        update = Update(db)
        try:
            update.add(_upt["update_id"])
            telegram.register_message(db, _upt["message"], token)
        except sqlite3.IntegrityError:
            print("Update ya registrado")

        pprint(_upt) # debug


if __name__ == "__main__":
    import sys

    try:
        action = sys.argv[1]
    except IndexError:
        print("Ingrese `init` `updates` o `send`")
        sys.exit(1)

    if action == "updates":
        get_updates()
    elif action == "send":
        try:
            chat_id = sys.argv[2]
            text = sys.argv[3]
        except IndexError:
            print("ingrese `chat_id` y `text` para enviar")
            sys.exit(1)

        telegram.send_message(text, int(chat_id), token)
    elif action == "init":
        db.setup_db([Update.table, Message.table])
    else:
        print("Ingrese `init` `updates` o `send`")
