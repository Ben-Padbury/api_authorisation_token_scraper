from api_authorisation_token import cacher
import api_authorisation_token.scraper.apple.podcasts as scraper

# Cache the bearer token.
cacher.cache(cacher.filename, scraper.get_bearer_token())