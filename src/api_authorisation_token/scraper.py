import abc
import string

from seleniumwire import webdriver
from seleniumwire.webdriver import Firefox


class Scraper(abc.ABC):
    api_scope = None
    timeout = None
    url = None

    def __init__(self):
        self.timeout = 90

    def scrape(self) -> string:
        with self._setup_web_driver() as driver:
            self._make_api_request(driver)

            # Wait for a request which contains the authorisation token, and return it.
            return driver.wait_for_request(self.api_scope, self.timeout).headers.get('Authorization')

    def _make_api_request(self, driver: Firefox) -> None:
        # By default, assume that the API request should be made just by making the initial connection, so do nothing.
        return None

    # Setup headless Firefox web driver.
    def _setup_web_driver(self) -> Firefox:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True

        # Reduce the scope of tracked requests to those to the API for podcasts. This way we can reasonably expect
        # the first request in the stack to be the one we want; bearing the auth token.
        driver = webdriver.Firefox(options=fireFoxOptions)
        driver.scopes = [self.api_scope]
        driver.get(self.url)

        return driver
