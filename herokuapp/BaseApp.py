from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def change_tab(self, tab_number):
        new_window = self.driver.window_handles[tab_number]
        return self.driver.switch_to.window(new_window)
