from api_authorisation_token.api.apple.podcasts import Podcasts

# Get an instance of the system we will be testing.
systemUnderTest = Podcasts()


def test_scrape():
    """Test that we get back a string that can reasonable be called an authorisation bearer token."""
    assert 'Bearer ' in systemUnderTest.scrape()
