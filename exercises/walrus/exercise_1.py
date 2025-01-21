import pprint
from utils.example_data import all_profiles

# pylint: disable=pointless-string-statement
"""
EXERCISE 1: DATASET TRANSFORM
------------------------

The code below transforms a dataset of profiles that looks like:
    [
        { 'age': int, 'gender': str, 'occupation': str, 'favourite_shop': str },
        ...
    ]

to a dataset of the number of favourite shops by occupation that looks like:
    {
        'occupation_1': {
            'shop_1': int,
            'shop_2': int,
            ...
        }
    }

where the `int`s are the total number of profiles with each shop in `favourite_shop`.

    * Use assignment expressions `:=` to make the code more concise.
        * The `assert` statements check your code for errors.
    * Once done, think about whether using `:=` improved this code.
        * What are the pros/cons of using `:=` here?

HINT: There are multiple ways of using `:=` (either in the `if` or using `.get`).
"""

shops_by_occup = {}

# YOUR CODE GOES HERE
for profile in all_profiles:
    occup = profile['occupation']
    if occup not in shops_by_occup:
        shops_by_occup[occup] = {}

    fav_shop = profile['favourite_shop']
    if fav_shop not in shops_by_occup[occup]:
        shops_by_occup[occup][fav_shop] = 0
    shops_by_occup[occup][fav_shop] += 1

print('Favourite shops by occupation:')
print('=' * 50)
pprint.pprint(shops_by_occup)

# <<< DO NOT CHANGE THE LINES BELOW HERE >>>
assert shops_by_occup['Brine surgeon']['Surfways'] == 64
assert shops_by_occup['Clameraman']['Algi'] == 133
assert shops_by_occup['Whaleway engineer']['sEabay'] == 70
