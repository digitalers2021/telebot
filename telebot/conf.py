import logging
import os

PWD = os.getcwd()
_LOG_LEVEl = os.getenv("BDR_LOG", "INFO")
_level = getattr(logging, _LOG_LEVEl)

logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s', level=_level)


def open_env():
    """
    Abre un archivo en el root del proyecto llamado ".env"
    y hace un parseo de las variables, las guarda en un diccionario
    options y tambien lo setea como variable de entorno
    """
    with open(f"{PWD}/.env", "r") as f:
        _envs = f.readlines()

    options = {}
    for x in _envs:
        k, v = x.split("=")
        os.environ[k] = v
        options.update({k: v.strip()})

    return options
