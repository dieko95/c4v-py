"""
    Base Persistency Manager: We need a way to handle persistency, 
    as simple files or maybe with a more complex scheme, such as databases
    or http requests. This base class provides a contract that
    every persistency manager should match in order to be used with our app.
"""

# Python imports
from typing import Iterator, List

# Local imports
from c4v.scraper.scraped_data_classes.scraped_data import ScrapedData


class BasePersistencyManager:
    """
        Base class to provide support for persistency management
    """

    def get_all(self) -> Iterator[ScrapedData]:
        """
            Return an iterator over the set of stored instances

            Return:
                Iterator of stored ScrapedData instances
        """
        raise NotImplementedError("Implement filter_scraped_urls abstract function")

    def filter_scraped_urls(self, urls: List[str]) -> List[str]:
        """
            Filter out urls whose data is already known, leaving only the ones to be scraped
            for first time
            Parameters: 
                urls : [str] = List of urls to filter 

            Return:
                A list of urls such that none of them has been scraped 
        """
        raise NotImplementedError("Implement filter_scraped_urls abstract function")

    def was_scraped(self, url: str) -> bool:
        """
            Tells if a given url is already scraped (it's related data is already know)
            Parameters:
                url : str = url to check if it was already scraped
            Return:
                If the given url's related data is already known
                
        """
        raise NotImplementedError("Implement was_scraped abstract function")

    def save(self, url_data: List[ScrapedData]):
        """
            Save provided data to local storage. 
            If some some urls are already in local storage, update them with provided new data.
            If not, delete them.
            Parameters:
                - data : [ScrapedData] = data to be saved
        """
        raise NotImplementedError("Implement save abstract method")

    def delete(self, urls: List[str]):
        """
            Delete provided urls from persistent storage
            Parameters:
                - urls : [str] = Urls to be deteled
        """
        raise NotImplementedError("Implement delete abstract method")
