from core.browser import ChromeBrowser
from config import config
from core.logger import Logger
from core.runner import Runner


def main():
    conf = config.setup()
    logger = Logger(conf.logging).logger
    driver = ChromeBrowser().driver
    runner = Runner(driver, conf, logger)

    runner.login()
    runner.navigate_to_network()
    suggestions = runner.get_suggestions()
    runner.connect_to_people(suggestions, 12)

    runner.end()
    logger.info("Stop program")


if __name__ == "__main__":
    main()
