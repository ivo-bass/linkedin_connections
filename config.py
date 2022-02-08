import yaml

from credentials import get_credentials


def get_configurations():
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
