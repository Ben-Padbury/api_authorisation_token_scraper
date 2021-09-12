import pytest
import scraper as sut

# Test that we get back an actual bearer token.
def test_output():
    assert 'Bearer ' in sut.get_bearer_token()