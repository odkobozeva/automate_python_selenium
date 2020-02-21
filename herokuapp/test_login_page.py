import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_login_pos(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/login')
    main_page.enter_data('tomsmith', 'SuperSecretPassword!')
    main_page.check_subheader('Welcome to the Secure Area. When you are done click logout below.')
    main_page.check_alert('You logged into a secure area!')
    time.sleep(2)
    main_page.logout()
    main_page.check_logout_alert('You logged out of the secure area!')


def test_login_wrong_name(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/login')
    main_page.enter_data('omsmith', 'SuperSecretPassword!')
    main_page.check_logout_alert('Your username is invalid!')
    main_page.check_h2('Login Page')
    time.sleep(2)


def test_login_wrong_password(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/login')
    main_page.enter_data('tomsmith', 'SuperSecretPassword')
    main_page.check_logout_alert('Your password is invalid!')
    time.sleep(2)


class SearchLocators:
    LOCATOR_USERNAME = (By.ID, "username")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_SUBMIT = (By.XPATH, "//*[@type='submit']")
    LOCATOR_SUBHEADER = (By.CLASS_NAME, "subheader")
    LOCATOR_LOGOUT = (By.XPATH, "//*[@href='/logout']")
    LOCATOR_ALERT = (By.ID, "flash")
    LOCATOR_LOGIN_PAGE = (By.TAG_NAME, "h2")


class BasePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class SearchHelper(BasePage):

    def enter_data(self, username, password):
        username_field = self.find_element(SearchLocators.LOCATOR_USERNAME)
        username_field.send_keys(username)
        password_field = self.find_element(SearchLocators.LOCATOR_PASSWORD)
        password_field.send_keys(password)
        submit_button = self.find_element(SearchLocators.LOCATOR_SUBMIT)
        submit_button.click()

    def check_subheader(self, text_subheader):
        subheader = self.find_element_wait(SearchLocators.LOCATOR_SUBHEADER).text
        assert subheader == text_subheader

    def check_alert(self, text_alert):
        alert = self.find_element_wait(SearchLocators.LOCATOR_ALERT).text
        assert text_alert in alert

    def logout(self):
        logout_button = self.find_element(SearchLocators.LOCATOR_LOGOUT)
        logout_button.click()

    def check_logout_alert(self, text_logout_alert):
        logout_alert = self.find_element_wait(SearchLocators.LOCATOR_ALERT).text
        assert text_logout_alert in logout_alert

    def check_h2(self, text_h2):
        h2 = self.find_element_wait(SearchLocators.LOCATOR_LOGIN_PAGE).text
        assert h2 == text_h2
