from api_authorisation_token.api.apple.podcasts import Podcasts

# Get an instance of the system we will be testing.
systemUnderTest = Podcasts()


# Test that we get back an actual bearer token.
def test_scrape():
    assert 'Bearer ' in systemUnderTest.scrape()
