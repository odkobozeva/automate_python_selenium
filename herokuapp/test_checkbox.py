import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_checkbox(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/checkboxes')
    main_page.select_all_checkbox()
    main_page.check_checkbox_condition('true')
    time.sleep(2)
    main_page.deselect_all_checkbox()
    main_page.check_checkbox_condition(None)
    time.sleep(5)


class SearchLocators:
    LOCATOR_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class SearchHelper(BasePage):

    def select_all_checkbox(self):
        all_checkbox = self.find_elements(SearchLocators.LOCATOR_CHECKBOX)
        for i in all_checkbox:
            if not i.get_attribute('checked'):
                i.click()

    def deselect_all_checkbox(self):
        all_checkbox = self.find_elements(SearchLocators.LOCATOR_CHECKBOX)
        for i in all_checkbox:
            if i.get_attribute('checked'):
                i.click()

    def check_checkbox_condition(self, checkbox_condition):
        all_checkbox = self.find_elements(SearchLocators.LOCATOR_CHECKBOX)
        for i in all_checkbox:
            t = i.get_attribute('checked')
            assert t == checkbox_condition
