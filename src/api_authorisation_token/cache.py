filename = 'authorisation_cache'

def cache(filename, value):
    # Open the cache file, based on the given filename, and write the value to it.
    with open(filename, 'w') as file:
        file.write(value)