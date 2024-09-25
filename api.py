import logging
import requests



class API:
    """Class to fetch data from API."""
    def __init__(self, api_url):
        self.log = logging.getLogger(__name__)
        self.api_url = api_url
        
    def fetch_data(self):
        """Fetch data from API"""
        try:
            data = requests.get(self.api_url)
            self.log.info(f"Fetching data from {self.api_url}")
            return data.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {self.api_url}: {e}")
            self.log.warning(f"Error fetching data from {self.api_url}: {e}")