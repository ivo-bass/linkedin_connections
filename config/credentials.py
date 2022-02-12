import os

import yaml


def read_credentials():
    with open("config/credentials.yaml") as file:
        credentials = yaml.safe_load(file)
    username = credentials['auth']['user']
    password = credentials['auth']['pass']
    return username, password


def prompt_credentials():
    username = input("Please write your email/phone: ")
    password = input("Please write your password: ")
    write_prompt = input("Write credentials to a file? [y/n]: ")
    if write_prompt in ('y', 'Y', 'yes', 'ъ', 'Ъ'):
        write_credentials(username, password)
    return username, password


def write_credentials(username, password):
    with open('config/credentials.yaml', 'w') as stream:
        yaml.safe_dump({'auth': {'user': username, 'pass': password}}, stream)


def get_credentials():
    if os.path.exists("config/credentials.yaml"):
        return read_credentials()
    return prompt_credentials()
