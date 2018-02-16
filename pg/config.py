#!/usr/bin/env python
# module: edgar/__init__.py
# author: Panagiotis Mavrogiorgos <pmav99,gmail>

import os
import logging.config
import pathlib

import yaml
try:
    from yaml import CLoader as YLoader
except ImportError:
    from yaml import YLoader
import munch

# paths
ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
CONFIG_FILE = (ROOT_DIR / "config.yaml").resolve()
_CONFIG = None


def apply_types(config):
    """ This is a hack, but having e.g. paths as Pathlib objects is convenient... :P """
    # load env variables
    for section, envs in config.env_vars.items():
        if section not in config:
            config[section] = munch.Munch()
        for env in envs:
            config[section][env.lower()] = os.environ.get(env)
    # connection_string
    if "database" in config:
        config.database["conn_str"] = "postgresql://{user}:{pass}@{host}:{port}/{db}".format(**config.database)
    print(config.database.conn_str)
    # convert paths to pathlib objects.
    for section in ("directories", "files"):
        if section in config:
            for key, value in config.directories.items():
                config.directories[key] = ROOT_DIR / value
    return config


def load_config(config_file):
    with open(config_file, "rb") as fd:
        config = yaml.load(fd, Loader=YLoader)
    return config


def get_config():
    """ Return the app's configuration. """
    global _CONFIG
    if _CONFIG is None:
        config = munch.munchify(load_config(CONFIG_FILE))
        config = apply_types(config)
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
