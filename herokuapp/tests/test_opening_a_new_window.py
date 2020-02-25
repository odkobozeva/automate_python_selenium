import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from herokuapp.BaseApp import BasePage


def test_new_window(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/windows')
    main_page.click_on_link()
    main_page.check_text('New Window')
    time.sleep(3)


class SearchLocators:
    LOCATOR_LINK = (By.XPATH, "//*[@href='/windows/new']")
    LOCATOR_TEXT = (By.TAG_NAME, "h3")


class SearchHelper(BasePage):

    def click_on_link(self):
        link = self.find_element(SearchLocators.LOCATOR_LINK)
        link.click()

    def check_text(self, text_new):
        self.change_tab(1)
        text = self.find_element(SearchLocators.LOCATOR_TEXT).text
        assert text == text_new
        self.driver.close()


