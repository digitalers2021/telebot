import logging
from pprint import pprint

import requests

from telebot.db import SQL
from telebot.models import Message


def send_message(msg, chatid, token):
    """ Manda mensaje a un usuario 

    token: es lo que debe estar en el .env
    """
    assert type(chatid) == int
    assert type(msg) == str
    assert type(token) == str

    BASE_URL = f"https://api.telegram.org/bot{token}"
    fullmsg = f"sendMessage?text={msg}&chat_id={chatid}"
    # query params
    rsp = requests.get(f"{BASE_URL}/{fullmsg}")
    logging.debug("Message sent %s", rsp.text)


def get_chat_id(username, token):
    """ have pull en base a un username 
    token: es lo que debe estar en el .env
    """

    BASE_URL = f"https://api.telegram.org/bot{token}"
    rsp = requests.get(f"{BASE_URL}/getUpdates")
    for r in rsp.json()["result"]:
        msg = r.get("message")
        if msg["from"]["username"] == username:
            id_ = msg["chat"]["id"]
            print(f"Chatid is: {id_}")
            return


def get_updates(token, offset=None):
    """ Obtiene todos los mensajes desde telegram
    API information: https://core.telegram.org/bots/api#getupdates
    Ejemplo de rsp.json()["result"]:
    [
    {'message': {'chat': {'first_name': 'Xavier',
                        'id': 222,
                        'last_name': 'Petit',
                        'type': 'private',
                        'username': 'xpetit'},
                'date': 1628086187,
                'from': {'first_name': 'Xavier',
                        'id': 3333,
                        'is_bot': False,
                        'language_code': 'en',
                        'last_name': 'Petit',
                        'username': 'xpetit'},
                'message_id': 7,
                'text': 'pepe'},
    'update_id': 478400752},
    ...
    ...
    ]
    """
    """agregado parametro de 'offset+1', updates ahora devuelve los mensajes sin ver
    """
    BASE_URL = f"https://api.telegram.org/bot{token}"
    rsp = requests.get(f"{BASE_URL}/getUpdates", params={'offset': offset+1})

    #pprint(rsp.json()["result"]) # debug

    return rsp.json()["result"]

def register_db(sql:SQL, data):
    msg = Message(sql)
    msg.add(data["chat"]["id"], data["message_id"], data["text"])

def send_txt(data, tkn):
    send_message(
        f"👋 Hola amigo {data['chat']['first_name']}! en que te puedo ayudar?",
        data["chat"]["id"], tkn)

def register_message(sql: SQL, data, tkn):
    """
        Para refactorizar la función register_message creamos dos nuevas funciones:
            register_db --> se encarga de guardar el mensaje en la base de datos
            send_txt  --> envía el mensaje de bienvenida
    """
    """
        Tomamos la excepción del error Key error para mandar el mensaje al usuario
    """
    
    try:
        register_db(sql, data)
        send_txt(data, tkn)
    except KeyError:
        send_message("No se admiten imagenes, tratá mandando un texto", data["chat"]["id"], tkn)
    