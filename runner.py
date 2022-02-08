import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


class Runner:
    def __init__(self, driver, conf) -> None:
        self.conf = conf
        self.driver = driver

    def login(self) -> None:
        self.driver.get(self.conf.login)

        username = self.driver.find_element(By.ID, "username")
        username.send_keys(self.conf.user)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys(self.conf.password)
        password.send_keys(Keys.ENTER)

    def navigate_to_network(self):
        self.driver.get(self.conf.network)
        time.sleep(10)

    def get_suggestions(self):
        suggestions = []
        try:
            suggestions = self.driver.find_elements(
                By.CSS_SELECTOR,
                "button.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.full-width",
            )
        except WebDriverException:
            print("SUGGESTIONS FAILED")
        finally:
            return suggestions

    def connect_to_people(self, suggestions, count):
        print("____________________________________")
        for number, person in enumerate(suggestions):
            if number == count:
                break
            try:
                person.click()
                print(person.get_attribute("aria-label").replace("to connect", "-> SUCCESS"))
                time.sleep(1)
            except WebDriverException:
                print(person.get_attribute("aria-label").replace("to connect", "-> FAIL"))
        print("____________________________________")

    def end(self):
        self.driver.close()
