import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_name(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/dropdown')
    main_page.check_default_select('Please select an option')
    main_page.choose_option('1', 'Option 1')
    time.sleep(5)
    main_page.choose_option('2', 'Option 2')
    time.sleep(4)


class SearchLocators:
    LOCATOR_SELECT = (By.ID, 'dropdown')
    LOCATOR_DEFAULT_SELECT = (By.XPATH, '//*[@id="dropdown"]/option[1]')
    LOCATOR_SELECT_STATUS = (By.XPATH, '//select/option[@selected]')


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class SearchHelper(BasePage):

    def check_default_select(self, default_select_text):
        default_select = self.find_element(SearchLocators.LOCATOR_DEFAULT_SELECT).text
        assert default_select == default_select_text

    def choose_option(self, option, text_option):
        select = Select(self.find_element(SearchLocators.LOCATOR_SELECT))
        select.select_by_value(option)
        select_status = self.find_element(SearchLocators.LOCATOR_SELECT_STATUS).text
        assert select_status == text_option
