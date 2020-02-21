import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_name(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/hovers')
    main_page.click_on_elems(browser)


class SearchLocators:
    LOCATOR_FIGURE = (By.XPATH, '//*[@class="figure"]')
    LOCATOR_VIEW_PROFILE = ".//*[contains(text(), 'View profile')]"
    LOCATOR_TEXT_PROFILE = (By.TAG_NAME, "h1")


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class SearchHelper(BasePage):

    def check_text_profile(self):
        return self.find_element(SearchLocators.LOCATOR_TEXT_PROFILE).text

    def counter_elements(self):
        return range(len(self.find_elements(SearchLocators.LOCATOR_FIGURE)))

    def click_on_elems(self, browser):
        for i in self.counter_elements():
            action = ActionChains(browser)
            elems = self.find_elements(SearchLocators.LOCATOR_FIGURE)
            action.move_to_element(elems[i]).perform()
            elems[i].find_element_by_xpath(SearchLocators.LOCATOR_VIEW_PROFILE).click()
            assert self.check_text_profile() == 'Not Found'
            browser.back()