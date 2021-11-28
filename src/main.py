from api_authorisation_token import cacher
from api_authorisation_token.scraper import Scraper
from api_authorisation_token.api.apple.podcasts import Podcasts
import argparse

# Setup argument parser; describing the program and arguments.
parser = argparse.ArgumentParser(description='This program scrapes the tokens from supported APIs.')
parser.add_argument(
    '-a',
    '--api',
    choices=['apple/podcasts'],
    metavar='API',
    required=True,
    help='The API to scrape the token from.'
)
arguments = parser.parse_args()


# Map the provided argument to an instance of a Scraper.
def map_api_to_scraper(name) -> Scraper:
    return {'apple/podcasts': Podcasts()}[name]


# Cache the bearer token.
cacher.cache(cacher.filename, map_api_to_scraper(arguments.api).scrape())
