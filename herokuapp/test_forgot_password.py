import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_forgot_password(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/forgot_password')
    main_page.enter_email('nalere4087@jmail7.com    ')
    time.sleep(3)
    main_page.check_text("Your e-mail's been sent!")
    time.sleep(3)


class SearchLocators:
    LOCATOR_INPUT = (By.TAG_NAME, "input")
    LOCATOR_BUTTON = (By.ID, "form_submit")
    LOCATOR_TEXT = (By.ID, "content")


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class SearchHelper(BasePage):

    def enter_email(self, email):
        email_field = self.find_element(SearchLocators.LOCATOR_INPUT)
        email_field.send_keys(email)
        button = self.find_element(SearchLocators.LOCATOR_BUTTON)
        button.click()

    def check_text(self, text_q):
        text = self.find_element(SearchLocators.LOCATOR_TEXT).text
        assert text == text_q
