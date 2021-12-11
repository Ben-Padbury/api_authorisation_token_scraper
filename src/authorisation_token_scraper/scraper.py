import string

from seleniumwire import webdriver
from seleniumwire.webdriver import Firefox


class Scraper():
    """The Scraper class is an abstract class that specifies the behaviour of any extending API token scrapers,
    including some default implementations.
    """

    api_scope = None
    """None|string The scope of the API we are scraping from. Used to restrict the captured requests, so that we only
         scrape the authorisation token for the expected API."""

    timeout = None
    """The timeout used by various internal processes, in seconds."""

    url = None
    """The URL we use t0o make the initial web driver connection. Should be to a destination we can reasonably
         be expected to make and capture API requests."""

    def __init__(self):
        self.timeout = 90

    def scrape(self) -> string:
        """Scrape the authorisation token for the given API scope of this scraper."""
        with self._setup_web_driver() as driver:
            self._make_api_request(driver)

            # Wait for a request which contains the authorisation token, and return it.
            return driver.wait_for_request(self.api_scope, self.timeout).headers.get('Authorization')

    def _make_api_request(self, driver: Firefox) -> None:
        """Make happen a request to the API scope that contains the authorisation token."""
        # By default, assume that the API request should be made just by making the initial connection, so do nothing.
        return None

    def _setup_web_driver(self) -> Firefox:
        """Set up the headless web driver used to make and capture requests."""
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True

        # Reduce the scope of tracked requests to those to the API for podcasts. This way we can reasonably expect
        # the first request in the stack to be the one we want; bearing the auth token.
        driver = webdriver.Firefox(options=fireFoxOptions)
        driver.scopes = [self.api_scope]
        driver.get(self.url)

        return driver
