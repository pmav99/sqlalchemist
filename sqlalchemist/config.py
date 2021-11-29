#!/usr/bin/env python
# module: pg/__init__.py
# author: Panagiotis Mavrogiorgos <pmav99,gmail>

import os
import logging.config
import pathlib

import munch
from ruyaml import YAML

yaml = YAML(typ="safe")

# paths
ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
CONFIG_FILE = (ROOT_DIR / "config.yaml").resolve()
_CONFIG = None


# _ENV_VARS = {
    # "database": ,
# }


def get_config():
    """Return the app's configuration."""
    global _CONFIG
    if _CONFIG is None:
        config = munch.munchify(yaml.load(CONFIG_FILE.read_text()))
        database_env_variables = ["DBHOST", "DBPORT", "DBUSER", "DBPASS", "DBNAME"]
        database = munch.munchify({key: os.environ[key]for key in database_env_variables})
        conn_str = f"postgresql://{database.DBUSER}:{database.DBPASS}@{database.DBHOST}:{database.DBPORT}/{database.DBNAME}"
        database["DB_CONNECTION_STRING"] = conn_str
        config.database = database
        _CONFIG = config
    return _CONFIG


def setup_logging():
    config = get_config()
    logging.config.dictConfig(config.logging)


setup_logging()

__all__ = [
    "get_config",
    "setup_logging",
]
