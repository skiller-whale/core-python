import re
import random
import time
from utils.example_data import whale_data

URL_PATTERN = re.compile('^https://skiller-whale.com/whales/(?P<whale_type>\w+)$')

class Response:
    """Web Response object."""
    def __init__(self, content, status_code):
        """
        Initialize a Response object.

        Args:
            content (dict): The content of the response.
            status_code (int): The status code of the response.
        """
        self.content = content
        self.status_code = status_code

    def __repr__(self) -> str:
        """
        Return a string representation of the Response object.

        Returns:
            str: A string representation of the Response object.
        """
        return f'Response(status_code={self.status_code}, content={self.content})'


def get(url):
    """
    Simulate a GET request to a given URL.

    Args:
        url (str): The URL to make the GET request to.

    Returns:
        Response: A Response object representing the response from the GET request.
    """
    # Sleep to simulate real requests
    time.sleep(random.random() * 0.25)

    if (match := URL_PATTERN.match(url)):
        if (whale_type := match['whale_type']) in whale_data:
            return Response(
                content={'num_sightings': whale_data[whale_type]},
                status_code=200
            )

    return Response(
        content={'error': f'No such whale type ({whale_type}).'},
        status_code=404
    )
