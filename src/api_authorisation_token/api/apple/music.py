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
        self.url = 'https://music.apple.com/gb/artist/rick-astley/669771'

    def get_bearer_token(self, driver: Firefox) -> string:
        # Wait for the button which makes a request to the API to be visible, and then click it.
        WebDriverWait(driver, self.timeout) \
            .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button.playback-button'))) \
            .move_to()

        # Wait for a request which contains the authorisation token, and return it.
        return driver.wait_for_request(self.api_scope, self.timeout).headers.get('Authorization')
