from seleniumwire import webdriver

# TODO: This currently only works for the podcast API. This may be a shared API token that works with the various APIs,
#  but if not we need to make this more generic.

try:
    # Setup headless Firefox web driver.
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    driver = webdriver.Firefox(options=fireFoxOptions)

    # Reduce the scope of tracked requests to those to the API for podcasts. This way we can reasonably expect
    # the first request in the stack to be the one we want; bearing the auth token.
    driver.scopes = ['https://amp-api.podcasts.apple.com/v1/*']
    driver.get('https://podcasts.apple.com/us/podcast/wrestling-with-johners-podcast/id1442108418')

    # Wait for a request which contains the authorisation token.
    request = driver.wait_for_request('https://amp-api.podcasts.apple.com/', 90)

    print(request.headers.get('Authorization'))
finally:
    # Try to close the driver, should it exist.
    if 'driver' in locals() and driver is not None:
        driver.close()
