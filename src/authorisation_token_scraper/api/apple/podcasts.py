from authorisation_token_scraper.scraper import Scraper


class Podcasts(Scraper):
    def __init__(self):
        super().__init__()
        self.api_scope = 'https://amp-api.podcasts.apple.com/'
        self.url = 'https://www.apple.com/apple-podcasts/'
