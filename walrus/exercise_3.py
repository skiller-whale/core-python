from utils import fake_requests

# pylint: disable=pointless-string-statement
"""
EXERCISE 3: WEB REQUESTS
------------------------

In this exercise you will retrieve some whale data using `fake_requests.get`.

There's an example call to `fake_requests.get` below. It returns a response object,
    which has two attributes:
    - `response.status_code`: `200` or `404`
    - `response.content`: dictionary if `status_code` is 200 - { 'num_sightings': int }

    * Use a single dictionary comprehension and `:=` to get the number of sightings
        for the  whale types in `WHALE_TYPES`.
        * You need to filter based on `status_code`.
        * Uncomment the assert statements to check your answers.
    * Once done, think about whether using `:=` improved your code.
        * What are the pros/cons of using `:=` here?

[EXTENSION]
    * Improve the `assert` statements using `:=`.
"""

# You can use `BASE_URL.format(<whale_type>)` to obtain valid URLs.
BASE_URL = 'https://skiller-whale.com/whales/{0}'
WHALE_TYPES = {
    'beluga',
    'fin_whale',
    'orca',
    'narwhal',
}

# Example call to `fake_requests.get`
response = fake_requests.get(BASE_URL.format('beluga'))
print(f'Beluga response: ({response.status_code}, {response.content})')

# * Use a single dictionary comprehension and `:=` to extract the number of sightings
#        for the  whale types in `WHALE_TYPES`.
whale_sightings = { ...: ... }


if __name__ == '__main__':
    for whale_type, num_sightings in whale_sightings.items():
        print(f'Whale sightings for {whale_type} - {num_sightings}')

    # # * Uncomment the assert statements to check your answers.
    # assert 'narwhal' in whale_sightings
    # assert whale_sightings['narwhal'] == 25, (
    #     f"Wrong num_sightings for 'narwhal' - {whale_sightings['narwhal']}, should be 25."
    # )

    # assert 'beluga' in whale_sightings
    # assert whale_sightings['beluga'] == 100, (
    #     f"Wrong num_sightings for 'beluga' - {whale_sightings['beluga']}, should be 100."
    # )
