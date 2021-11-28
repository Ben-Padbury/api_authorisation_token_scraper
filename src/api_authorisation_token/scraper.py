import abc
import string

from seleniumwire import webdriver
from seleniumwire.webdriver import Firefox


class Scraper(abc.ABC):    
    def __init__(self):
        self.api_scope = None
        self.timeout = 120
        self.url = None

    @classmethod
    @abc.abstractmethod
    def get_bearer_token(cls, driver: Firefox) -> string:
        pass

    def scrape(self) -> string:
        try:
            driver = self.setup_web_driver()
            return self.get_bearer_token(driver)
        finally:
            # Try to close the driver, should it exist.
            if 'driver' in locals() and driver is not None:
                driver.close()

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
