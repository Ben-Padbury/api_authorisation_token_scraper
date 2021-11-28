from api_authorisation_token import cacher
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

# Cache the bearer token.
cacher.cache(cacher.filename, Podcasts().scrape())
