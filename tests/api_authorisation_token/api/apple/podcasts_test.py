import os
import sys

# Add system under test to system path so that we can test it.
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'src'
    )
)

from api_authorisation_token.api.apple.podcasts import Podcasts

# Get an instance of the system we will be testing.
systemUnderTest = Podcasts()

# Test that we get back an actual bearer token.
def test_scrape():
    assert 'Bearer ' in systemUnderTest.scrape()
