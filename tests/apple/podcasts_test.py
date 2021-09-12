import os
import pytest
import sys

# Add system under test to system path so that we can test it.
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'api_authorisation_token_scraper'
    )
)


import apple.podcasts as sut

# Test that we get back an actual bearer token.
# def test_output():
#     assert 'Bearer ' in sut.get_bearer_token()