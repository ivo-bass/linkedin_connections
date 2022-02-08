import yaml


def get_configurations():
    with open("config.yaml") as config_file:
        return yaml.safe_load(config_file)


class Config:
    def __init__(self):
        configurations = get_configurations()
        self.user = configurations["auth"]["user"]
        self.password = configurations["auth"]["pass"]
        self.driver_path = configurations["driver_path"]
        self.login = configurations["url"]["login"]
        self.network = configurations["url"]["network"]
