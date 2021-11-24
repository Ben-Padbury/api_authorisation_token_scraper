from seleniumwire import webdriver
from selenium.webdriver.common.by import By


def get_bearer_token():
    try:
        # Setup headless Firefox web driver.
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True
        driver = webdriver.Firefox(options=fireFoxOptions)

        # Reduce the scope of tracked requests to those to the API for podcasts. This way we can reasonably expect
        # the first request in the stack to be the one we want; bearing the auth token.
        driver.scopes = ['https://amp-api.podcasts.apple.com/v1/*']
        driver.get('https://podcasts.apple.com/us/podcast/wrestling-with-johners-podcast/id1442108418')

        # Find the button which makes a request to the API and click it.
        driver.find_element(By.CSS_SELECTOR, 'button.link:nth-child(1)').click()

        # Wait for a request which contains the authorisation token.
        request = driver.wait_for_request('https://amp-api.podcasts.apple.com/', 90)
        print(request.method)

        return request.headers.get('Authorization')
    finally:
        # Try to close the driver, should it exist.
        if 'driver' in locals() and driver is not None:
            driver.close()
