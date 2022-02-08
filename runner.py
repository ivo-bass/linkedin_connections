import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Runner:
    def __init__(self, driver, conf) -> None:
        self.conf = conf
        self.driver = driver

    def login(self) -> None:
        # Load loggin page
        self.driver.get(self.conf.login)

        # Get the login element and write username
        username = self.driver.find_element(By.ID, "username")
        username.send_keys(self.conf.user)

        # Get the password element, write password and hit ENTER
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(self.conf.password)
        password.send_keys(Keys.ENTER)

    def navigate_to_network(self):
        self.driver.get(self.conf.network)
        time.sleep(10)

    def get_suggestions(self):
        suggestions = []
        try:
            print("____________________________________")
            suggestions = self.driver.find_elements(
                By.CSS_SELECTOR,
                "button.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.full-width",
            )
            print(suggestions)
        except:
            print("FAILED")
        finally:
            print("____________________________________")
            return suggestions

    def connect_to_people(self, suggestions, count):
        if not suggestions:
            return
        for number, person in enumerate(suggestions):
            if number == count:
                break
            print(person.get_attribute("aria-label").replace(" to connect", "-> DONE"))
            person.click()
        time.sleep(10)

    def end(self):
        self.driver.close()
