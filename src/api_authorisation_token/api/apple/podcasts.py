from api_authorisation_token.scraper import Scraper
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import string


class Podcasts(Scraper):
    def scrape(self) -> string:
        try:
            # Setup headless Firefox web driver.
            fireFoxOptions = webdriver.FirefoxOptions()
            fireFoxOptions.headless = True
            driver = webdriver.Firefox(options=fireFoxOptions)

            # Reduce the scope of tracked requests to those to the API for podcasts. This way we can reasonably expect
            # the first request in the stack to be the one we want; bearing the auth token.
            driver.scopes = ['https://amp-api.podcasts.apple.com/v1/*']
            driver.get('https://podcasts.apple.com/us/podcast/wrestling-with-johners-podcast/id1442108418')

            # Wait for the button which makes a request to the API to be visible, and then click it.
            WebDriverWait(driver, 120)\
                .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button.link:nth-child(1)')))\
                .click()

            # Wait for a request which contains the authorisation token.
            request = driver.wait_for_request('https://amp-api.podcasts.apple.com/', 120)

            return request.headers.get('Authorization')
        finally:
            # Try to close the driver, should it exist.
            if 'driver' in locals() and driver is not None:
                driver.close()
