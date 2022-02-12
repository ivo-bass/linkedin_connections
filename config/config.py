from dataclasses import dataclass

import yaml

from config.credentials import get_credentials


@dataclass
class Config:
    user: str = None
    password: str = None
    urls: dict = None
    logging: dict = None


def setup():
    user, password = get_credentials()
    urls, logging = get_configurations()
    return Config(user, password, urls, logging)


def get_configurations():
    with open("config/config.yaml") as config_file:
        configurations = yaml.safe_load(config_file)
    urls = configurations["urls"]
    logging = configurations["logging"]
    return urls, logging
