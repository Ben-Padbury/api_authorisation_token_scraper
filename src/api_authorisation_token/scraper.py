import abc
import string

from seleniumwire import webdriver
from seleniumwire.webdriver import Firefox


class Scraper(abc.ABC):    
    def __init__(self):
        self.api_scope = None
        self.timeout = 90
        self.url = None

    @classmethod
    @abc.abstractmethod
    def make_api_request(cls, driver: Firefox) -> string:
        pass

    def scrape(self) -> string:
        with self.setup_web_driver() as driver:
            self.make_api_request(driver)

            # Wait for a request which contains the authorisation token, and return it.
            return driver.wait_for_request(self.api_scope, self.timeout).headers.get('Authorization')

    # Setup headless Firefox web driver.
    def setup_web_driver(self) -> Firefox:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True

        # Reduce the scope of tracked requests to those to the API for podcasts. This way we can reasonably expect
        # the first request in the stack to be the one we want; bearing the auth token.
        driver = webdriver.Firefox(options=fireFoxOptions)
        driver.scopes = [self.api_scope]
        driver.get(self.url)

        return driver
