import string

from api_authorisation_token.scraper import Scraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire.webdriver import Firefox


class Music(Scraper):
    def __init__(self):
        super().__init__()
        self.api_scope = 'https://amp-api.music.apple.com/'
        self.url = 'https://music.apple.com/gb/browse'

    def make_api_request(self, driver: Firefox) -> string:
        # Wait for the button which makes a request to the API to be visible, and then click it.
        WebDriverWait(driver, self.timeout) \
            .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'div[role=link]'))) \
            .click()
