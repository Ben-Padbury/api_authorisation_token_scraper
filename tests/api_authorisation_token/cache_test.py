import os
import pytest
import random
import string
import sys

# Add system under test to system path so that we can test it.
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'src'
    )
)


import api_authorisation_token.cache as sut

# Test that we get back an actual bearer token.
def test_cache():
    filename = sut.filename + '.test'
    value = random_string()
    sut.cache(filename, value)
    assert os.path.exists(filename)
    with open(filename, 'r') as file:
        assert value == file.readlines()[-1]

# Generate a random string for a given length and character source.
def random_string(length=32, source=string.ascii_lowercase):
    return ''.join(random.choice(source) for i in range(length))
