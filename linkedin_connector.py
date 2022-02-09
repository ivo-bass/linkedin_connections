import time

from browser import ChromeBrowser
from config import setup
from logger import Logger
from runner import Runner


def main():
    config = setup()
    logger = Logger(config.logging).logger
    logger.info("Start program")

    driver = ChromeBrowser().driver

    runner = Runner(driver, config, logger)
    runner.login()
    runner.navigate_to_network()
    suggestions = runner.get_suggestions()
    runner.connect_to_people(suggestions, 8)

    time.sleep(3)
    runner.end()
    logger.info("Stop program")


if __name__ == "__main__":
    main()
