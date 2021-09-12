import api_authorisation_token_scraper.apple.podcasts as scraper

with open('authorisation_cache', 'w+') as file:
    file.write(scraper.get_bearer_token())
