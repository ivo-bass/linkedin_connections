import yaml


def store_credentials(username, password):
    with open('config.yaml', 'r+') as stream:
        data = yaml.safe_load(stream)
        if data.get('auth'):
            return
        yaml.safe_dump({'auth': {'user': username, 'pass': password}}, stream)


def get_credentials():
    username = input("Please write your email/phone: ")
    password = input("Please write your password: ")
    write_prompt = input("Store credentials to config file? [y/n]: ")
    if write_prompt in ('y', 'Y', 'yes', 'ъ', 'Ъ'):
        store_credentials(username, password)
    return username, password
