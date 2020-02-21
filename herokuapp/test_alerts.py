import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_name(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/javascript_alerts')
    main_page.click_for_alert()
    main_page.click_for_confirm_accept()
    main_page.click_for_confirm_dismiss()
    main_page.click_for_prompt_enter_text()
    main_page.click_for_prompt_dismiss()


class SearchLocators:
    LOCATOR_ALERT = (By.XPATH, "*//button[contains(text(), 'Click for JS Alert')]")
    LOCATOR_CONFIRM = (By.XPATH, "*//button[contains(text(), 'Click for JS Confirm')]")
    LOCATOR_PROMPT = (By.XPATH, "*//button[contains(text(), 'Click for JS Prompt')]")
    LOCATOR_RESULT = (By.ID, "result")


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def check_result(self, text_result):
        result = self.find_element(SearchLocators.LOCATOR_RESULT).text
        assert result == text_result
        print(result)


class SearchHelper(BasePage):

    def click_for_alert(self):
        button = self.find_element(SearchLocators.LOCATOR_ALERT)
        button.click()
        self.switch_to_alert().accept()
        self.check_result('You successfuly clicked an alert')

    def click_for_confirm_accept(self):
        button = self.find_element(SearchLocators.LOCATOR_CONFIRM)
        button.click()
        self.switch_to_alert().accept()
        self.check_result('You clicked: Ok')

    def click_for_confirm_dismiss(self):
        button = self.find_element(SearchLocators.LOCATOR_CONFIRM)
        button.click()
        self.switch_to_alert().dismiss()
        self.check_result('You clicked: Cancel')

    def click_for_prompt_enter_text(self):
        button = self.find_element(SearchLocators.LOCATOR_PROMPT)
        button.click()
        self.switch_to_alert().send_keys('some text')
        self.switch_to_alert().accept()
        self.check_result('You entered: some text')

    def click_for_prompt_dismiss(self):
        button = self.find_element(SearchLocators.LOCATOR_PROMPT)
        button.click()
        self.switch_to_alert().dismiss()
        self.check_result('You entered: null')


