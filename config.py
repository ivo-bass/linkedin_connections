import os

import yaml

from credentials import get_credentials


def write_configurations():
    with open("config.yaml", "w") as file:
        data = {"url": {
            "login": "http://linkedin.com/login",
            "network": "https://www.linkedin.com/mynetwork/"}
        }
        yaml.safe_dump(data, file)


def get_configurations():
    if not os.path.exists("config.yaml"):
        write_configurations()
    with open("config.yaml") as config_file:
        configurations = yaml.safe_load(config_file)
    if not configurations.get('auth'):
        username, password = get_credentials()
        configurations['auth'] = {'user': username, 'pass': password}
    return configurations


class Config:
    def __init__(self):
        configurations = get_configurations()
        self.user = configurations["auth"]["user"]
        self.password = configurations["auth"]["pass"]
        self.login = configurations["url"]["login"]
        self.network = configurations["url"]["network"]
