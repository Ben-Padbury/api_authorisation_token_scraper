from authorisation_token_scraper.scraper import Scraper


class Podcasts(Scraper):
    """The Podcasts class is an extension of the Scraper class that is designed for scraping the authorisation token
     from the Apple Podcasts API.
     """

    def __init__(self):
        super().__init__()
        self.api_scope = 'https://amp-api.podcasts.apple.com/'
        self.url = 'https://www.apple.com/apple-podcasts/'
