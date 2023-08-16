from utils import fake_requests

# pylint: disable=pointless-string-statement
"""
EXERCISE 4: WITNESSES
------------------------

In this exercise you will retrieve some whale data using `fake_requests.get`.

The convenience function `request_whale_info` can be used to obtain information
    about a whale type. It returns a `Response` object with the following attributes:
    - `response.status_code`: `200` or `404`
    - `response.content`: a dictionary
        - { 'num_sightings': int } if `response.status_code == 200`
        - { 'error': str } if `response.status_code == 404`

    * Use a single call to `any` to find whether there is a whale
        with fewer than `25` sightings.
        * If so, also find the "witness", which is any such whale.
        * Replace `whale_type` and `num_sightings` with the type and
            number of sightings of the "witness".
    * Once done, think about whether using `:=` improved your code.
        * What are the pros/cons of using `:=` here?

HINT: Start with the solution to the previous exercise.
    Can you create a "witness" object inside the call to `any`?
"""

# You can use `base_url.format(<whale_type>)` to obtain valid URLs.
BASE_URL = 'https://skiller-whale.com/whales/{0}'
WHALE_TYPES = [
    'beluga',
    'fin_whale',
    'orca',
    'narwhal',
    'humpback',
    'fin',
    'bowhead',
    'blue',
    'minkle',
    'sei',
    'gray'
]


def request_whale_info(whale_type):
    """Convenience function to send a request for whale info."""
    url = BASE_URL.format(whale_type)
    return fake_requests.get(url)


# Example call to `request_whale_info.get`
response = request_whale_info('beluga')
print(f'Beluga response: ({response})')

# * Use a single call to `any` to find whether there is a whale
#     with fewer than `25` sightings.
#   * If so, also find the "witness", which is any such whale.
#   * Replace `whale_type` and `num_sightings` with the type and
#       number of sightings of the "witness".
if any(...):
    print((
        'There is a whale with fewer than 25 sightings',
        f" - {whale_type}, {num_sightings}"
    ))
