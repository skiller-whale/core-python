from utils import fake_requests

# pylint: disable=pointless-string-statement
"""
EXERCISE 4: WITNESSES
------------------------

In this exercise you will retrieve some whale data using `fake_requests.get`.

There's an example call to `fake_requests.get` below. It returns a response object,
    which has two attributes:
    - `response.status_code`: `200` or `404`
    - `response.content`: dictionary if `status_code` is 200 - { 'num_sightings': int }

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

# Example call to `fake_requests.get`
response = fake_requests.get(BASE_URL.format('beluga'))
print(f'Beluga response: ({response.status_code}, {response.content})')

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
