import time

from config import Config
from browser import ChromeBrowser
from runner import Runner


def main():
    conf = Config()

    driver = ChromeBrowser().driver

    run = Runner(driver, conf)

    run.login()
    run.navigate_to_network()
    suggestions = run.get_suggestions()
    run.connect_to_people(suggestions, 8)

    time.sleep(3)

    run.end()


if __name__ == "__main__":
    main()
