import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from herokuapp.BaseApp import BasePage


@pytest.mark.parametrize('keys', [
                                    ['\ue023', 'NUMPAD9'],
                                    ['\ue008', 'SHIFT'],
                                    ['\ue031', 'F1'],
                                    ['`', 'BACK_QUOTE'],
                                    ['\ue013', 'UP']
                                  ])
def test_key_press(browser, keys):
    main_page = SearchHelper(browser)
    main_page.go_to_site('https://the-internet.herokuapp.com/key_presses')
    main_page.enter_key(keys)
    time.sleep(5)


class SearchLocators:
    LOCATOR_INPUT = (By.ID, "target")
    LOCATOR_RESULT = (By.ID, "result")


class SearchHelper(BasePage):

    def enter_key(self, keys):
        input = self.find_element(SearchLocators.LOCATOR_INPUT)
        result = self.find_element(SearchLocators.LOCATOR_RESULT)
        input.send_keys(keys[0])
        assert result.text == f'You entered: {keys[1]}'
