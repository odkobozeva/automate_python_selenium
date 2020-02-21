import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_new_window(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/windows')
    main_page.click_on_link()
    main_page.check_text('New Window')
    time.sleep(3)


class SearchLocators:
    LOCATOR_LINK = (By.XPATH, "//*[@href='/windows/new']")
    LOCATOR_TEXT = (By.TAG_NAME, "h3")


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def change_tab(self, tab_number):
        new_window = self.driver.window_handles[tab_number]
        return self.driver.switch_to.window(new_window)


class SearchHelper(BasePage):

    def click_on_link(self):
        link = self.find_element(SearchLocators.LOCATOR_LINK)
        link.click()

    def check_text(self, text_new):
        self.change_tab(1)
        text = self.find_element(SearchLocators.LOCATOR_TEXT).text
        assert text == text_new
        self.driver.close()


