from api_authorisation_token.scraper import Scraper
from api_authorisation_token.api.apple.podcasts import Podcasts
import argparse

# Define a dictionary of the supported APIs, linking a human readable/writable identifier to the Scraper implementation.
apis = dict[str, Scraper]([('apple/podcasts', Podcasts)])

# Setup argument parser; describing the program and arguments. Then parse out the arguments.
parser = argparse.ArgumentParser(description='This program scrapes the tokens from supported APIs.')
parser.add_argument(
    '-a',
    '--api',
    choices=apis.keys(),
    required=True,
    help='The API to scrape the token from.'
)
arguments = parser.parse_args()

# Print the bearer token.
print(apis[arguments.api]().scrape())
