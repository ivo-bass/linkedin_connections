import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


class Runner:
    def __init__(self, driver, conf, logger) -> None:
        self.driver = driver
        self.conf = conf
        self.logger = logger

    def login(self) -> None:
        self.driver.get(self.conf.urls["login"])
        self.logger.info("Navigated to Login")

        username = self.driver.find_element(By.ID, "username")
        username.send_keys(self.conf.user)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys(self.conf.password)
        password.send_keys(Keys.ENTER)

    def navigate_to_network(self):
        self.driver.get(self.conf.urls["network"])
        self.logger.info("Navigated to Network")
        time.sleep(10)

    def get_suggestions(self):
        suggestions = []
        try:
            suggestions = self.driver.find_elements(
                By.CSS_SELECTOR,
                "button.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.full-width",
            )
            self.logger.info("SUGGESTIONS SUCCESS")
        except WebDriverException:
            self.logger.error("SUGGESTIONS FAILED")
        finally:
            return suggestions

    def connect_to_people(self, suggestions, count):
        for number, person in enumerate(suggestions):
            if number == count:
                break
            try:
                person.click()
                self.logger.info(person.get_attribute("aria-label").replace("to connect", "-> SUCCESS"))
                time.sleep(1)
            except WebDriverException:
                self.logger.error(person.get_attribute("aria-label").replace("to connect", "-> FAIL"))

    def end(self):
        self.driver.close()
        self.logger.info("Browser closed")
