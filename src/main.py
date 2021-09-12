import api_authorisation_token_scraper.apple.podcasts as scraper

# Open the cache file and write the bearer token to it.
with open('authorisation_cache', 'w') as file:
    file.write(scraper.get_bearer_token())
