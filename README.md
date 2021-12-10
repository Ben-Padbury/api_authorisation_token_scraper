# Authorisation token scraper

A python script to scrape various authorisation bearer tokens for use externally. Currently, only supports predefined
APIs.

## Driver

This scraper makes use of a Firefox headless browser, which requires `mozzila/geckodriver`, which needs to be installed
before the scraper can be run. Make sure it’s in your PATH, e.g. place it in `/usr/bin` or `/usr/local/bin`.

Failure to observe this step will give you an error `selenium.common.exceptions.WebDriverException:
Message:‘geckodriver’ executable needs to be in PATH`.

## APIs

The supported APIs are listed below. If there are multiple APIs from the same source/company, then they will be
collected under a subsection.

#### Apple

- Music
- Podcasts