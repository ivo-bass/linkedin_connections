from config import Config
from driver import ChromeDriver
from runner import Runner


def main():
    conf = Config()

    driver = ChromeDriver(conf.driver_path).driver

    run = Runner(driver, conf)

    run.login()
    run.navigate_to_network()
    suggestions = run.get_suggestions()
    run.connect_to_people(suggestions, 10)
    run.end()


if __name__ == "__main__":
    """"""
    main()
