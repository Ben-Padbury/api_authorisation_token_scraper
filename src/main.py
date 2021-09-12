import api_authorisation_token.scraper.apple.podcasts as scraper
import api_authorisation_token.cache

# Cache the bearer token.
cache.cache(cache.filename, scraper.get_bearer_token())