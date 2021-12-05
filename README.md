# API authorisation token scraper

A python script to scrape various API authorisation bearer tokens.

## How to use
### Choosing the API
When calling the script the API you want to scrape the authorisation token from is dictated by the API argument, either
`--api` or `-a`. For example, if you wanted the token from the Apple Music API you would run this on the command line
`python api_authorisation_token_scraper -a apple/music` which would output something like this:
`Bearer <token>`.

## Supported APIs 
- Apple
  - Music 
  - Podcasts
