import abc
import string


class Scraper(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def scrape(cls) -> string:
        pass
