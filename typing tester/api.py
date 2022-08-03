"""
The file contains the RandomWords class.
The class can be used to retrieve random words from random-words-with-pronunciation
hosted at rapidapi.com.
"""
import json
import requests
from constants import URL, X_RAPIDAPI_KEY, X_RAPIDAPI_HOST

class RandomWords:
    """
    The RandomWords retreives data from the random-words-with-pronunciation API

    Attributes:
        url (str):
        x_rapidapi_key (str): Contains the hashkey for the random words with pronunciation API.
        x_rapidapi_host (str): Contains the hostname for the random words with pronunciation API.
        
    Methods:
        fetch_random_words: Requests the API with Get method and Returns the
        data fetched from the API call.
    """
    def __init__(self):
        """ 
        Initializes the class object and stores the host url and headers.

        Arguments:
            url (str): The url for the API host
            x_rapidapi_key (str): Contains the hashkey for the random words with pronunciation API.
            x_rapidapi_host (str): Contains the hostname for the random words with pronunciation API.
        """
        self.url = URL
        self.x_rapidapi_key = X_RAPIDAPI_KEY
        self.x_rapidapi_host = X_RAPIDAPI_HOST

    def preapre_header(self):
        """
        This function prepares the header for the API call.

        Arguments:
            None

        Returns:
            headers (dict): The header contains the key and hsot name.
        """
        headers = {
            "x-rapidapi-key" : self.x_rapidapi_key,
            "x-rapidapi-host": self.x_rapidapi_host
        }

        return headers


    def fetch_random_words(self):
        """
        The function calls the API with the GET method and then parses the responce json to 
        extract the data and returns it.

        Arguments:
            None

        Returns:
            data (dict): Contains the data fetched from the api call in form of key value pairs.  
            error (str): Incase the API call fails due to any reason, the error messages is returned.
        """
        headers = self.preapre_header()
        try:
            response = requests.get(self.url, headers=headers)
            data = json.loads(response.text)[0]
            return data
        except Exception as exp:
            return (f"API Request Error: {exp}")

