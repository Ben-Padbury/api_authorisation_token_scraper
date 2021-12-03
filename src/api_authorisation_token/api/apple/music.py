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
        self.timeout = 300
        self.url = 'https://music.apple.com/gb/album/whenever-you-need-somebody/1558533900'

    def get_bearer_token(self, driver: Firefox) -> string:
        # Wait for the body to gain the 'album' class, which to my best understanding indicates that the javascript
        # application chunks have loaded, which should add the required event listener.
        element = WebDriverWait(driver, self.timeout) \
            .until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'body')))
        WebDriverWait(driver, self.timeout).until(lambda d: 'album' in element.get_attribute('class'))

        # Wait for the button which makes a request to the API to be visible, and then click it.
        WebDriverWait(driver, self.timeout) \
            .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button.play-button')))

        # Wait for a request which contains the authorisation token, and return it.
        return driver.wait_for_request(self.api_scope, self.timeout).headers.get('Authorization')
