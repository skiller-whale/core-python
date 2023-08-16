from utils import fake_requests

# pylint: disable=pointless-string-statement
"""
EXERCISE 3: WEB REQUESTS
------------------------

In this exercise you will retrieve some whale data using `fake_requests.get`.

The convenience function `request_whale_info` can be used to obtain information
    about a whale type. It returns a `Response` object with the following attributes:
    - `response.status_code`: `200` or `404`
    - `response.content`: a dictionary
        - { 'num_sightings': int } if `response.status_code == 200`
        - { 'error': str } if `response.status_code == 404`

Currently a for loop is used to extract the number of sightings of whale types.

    * Rewrite this for loop using a single dictionary comprehension and `:=`.

    * Once done, think about whether using `:=` improved your code.
        * What are the pros/cons of using `:=` here?

[EXTENSION]
    * Improve the `assert` statements using `:=`.
"""

BASE_URL = 'https://skiller-whale.com/whales/{0}'
WHALE_TYPES = {
    'beluga',
    'fin_whale',
    'orca',
    'narwhal',
}


def request_whale_info(whale_type):
    """Convenience function to send a request for whale info."""
    url = BASE_URL.format(whale_type)
    return fake_requests.get(url)


# * Rewrite this for loop using a single dictionary comprehension and `:=`.
whale_sightings = { }
for whale_type in WHALE_TYPES:
    # request whale info for `whale_type`.
    response = request_whale_info(whale_type)

    # * You can uncomment this print statement to examine the responses.
    # print(response)

    # Only use responses if the status is `200`.
    #   For some whale types there is no data.
    if response.status_code == 200:
        # Extract and store `num_sightings` from the content of the response.
        whale_sightings[whale_type] = response.content['num_sightings']

if __name__ == '__main__':
    for whale_type, num_sightings in whale_sightings.items():
        print(f'Whale sightings for {whale_type} - {num_sightings}')

    assert 'narwhal' in whale_sightings
    assert whale_sightings['narwhal'] == 25, (
        f"Wrong num_sightings for 'narwhal' - {whale_sightings['narwhal']}, should be 25."
    )

    assert 'beluga' in whale_sightings
    assert whale_sightings['beluga'] == 100, (
        f"Wrong num_sightings for 'beluga' - {whale_sightings['beluga']}, should be 100."
    )
