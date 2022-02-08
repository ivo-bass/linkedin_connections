from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ChromeDriver:
    def __init__(self, path: str) -> None:
        self.service = Service(path)
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
