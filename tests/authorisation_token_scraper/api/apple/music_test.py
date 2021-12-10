from authorisation_token_scraper.api.apple.music import Music

# Get an instance of the system we will be testing.
systemUnderTest = Music()


# Test that we get back an actual bearer token.
def test_scrape():
    assert 'Bearer ' in systemUnderTest.scrape()
