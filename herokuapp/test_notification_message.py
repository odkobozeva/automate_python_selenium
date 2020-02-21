import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_name(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/notification_message_rendered')
    text = ''
    while 'Action successful' not in text:
        main_page.click_button()
        text = main_page.check_text()


class SearchLocators:
    LOCATOR_NOTIFICATION = (By.ID, "flash")
    LOCATOR_BUTTON = (By.XPATH, '//*[@href="/notification_message"]')


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class SearchHelper(BasePage):

    def click_button(self):
        button = self.find_element(SearchLocators.LOCATOR_BUTTON)
        button.click()

    def check_text(self):
        return self.find_element(SearchLocators.LOCATOR_NOTIFICATION).text