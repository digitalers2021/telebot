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


def get_updates(token):
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
    BASE_URL = f"https://api.telegram.org/bot{token}"
    rsp = requests.get(f"{BASE_URL}/getUpdates")

    # pprint(rsp.json()["result"]) # debug

    return rsp.json()["result"]


def register_message(sql: SQL, data, tkn):
    """
    Recibe un mensaje, lo guarda en la base y envia 
    un response.
    {'chat': {'first_name': 'Xavier',
                      'id': 44444,
                      'last_name': 'Petit',
                      'type': 'private',
                      'username': 'xpetit'
             },
     'date': 1628087051,
     'from': {'first_name': 'Xavier',
                      'id': 4444,
                      'is_bot': False,
                      'language_code': 'en',
                      'last_name': 'Petit',
                      'username': 'xpetit'},
     'message_id': 15,
     'text': 'dame info'}
    """
    msg = Message(sql)
    msg.add(data["chat"]["id"], data["message_id"], data["text"])
    send_message(
        f"👋 Hola {data['chat']['first_name']}! en que te puedo ayudar?",
        data["chat"]["id"], tkn)
