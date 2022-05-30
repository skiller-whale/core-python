from pprint import pprint

from example_data import all_profiles


"""
1. INTRODUCTION TO TUPLES
-------------------------

Update the function `tuple_from_profile` so that it takes a dict, `profile`,
and return a tuple which contains the values for:
    * occupation
    * age
    * gender
    * favourite_shop

Example usage:

    >>> tuple_from_profile({
            'name': 'Shark Ruffalo',
            'occupation': 'Trout',
            'age': '40-50',
            'gender': 'M',
            'favourite_shop': 'Algi',
        })

    ('Trout', '40-50', 'M', 'Algi')
"""


def tuple_from_profile(profile):
    # TODO complete this function.
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE >>>

example_profile = {
    'name': 'Free Willy Nelson',
    'occupation': 'Guitarfish',
    'age': '60+',
    'gender': 'M',
    'favourite_shop': 'Sharks and Spencer',
}

profile_attributes = tuple_from_profile(example_profile)
print("Attributes are:", profile_attributes)


"""
2. TUPLES AS KEYS
-----------------

Uncomment the three lines of code at the bottom of this section.

The variable `all_profiles` is a large list containing customer profile dicts
(like the ones you have seen in earlier exercises).

Update the function `get_largest_segment` so that it returns:

1. The most common profile in terms of (occupation, age, gender, favourite_shop).
2. The number of customers with that profile.

For example:

  >>> get_largest_segment([
      {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish'},
      {'occupation': 'Eelectrician', 'age': '10-20', 'gender': 'F', 'favourite_shop': 'Surfways'},
      {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish'},
  ])

  Should return:

  {'occupation': 'Pilot whale', 'age': '30-40', 'gender', 'F', 'favourite_shop': 'John Lewfish'}, 2

You can (should) use the functions `tuple_from_profile`, `dict_from_tuple` and
`largest_value_and_key` to help you.
"""


# This function is the reverse of the one you wrote in exercise 1.
# You do not need to change it.
def dict_from_tuple(attributes):
    """Create a dictionary from a given tuple"""
    occupation, age, gender, favourite_shop = attributes
    return {
        'occupation': occupation,
        'age': age,
        'gender': gender,
        'favourite_shop': favourite_shop,
    }


# This function is provided to help you - you do not need to change it.
def largest_value_and_key(d):
    """Return the largest value in dict `d`, and its key (inefficient implementation)"""
    max_value = max(d.values())
    for key, value in d.items():
        if value == max_value:
            return value, key


def get_largest_segment(profiles):
    # TODO: complete this function
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# largest_segment, frequency = get_largest_segment(all_profiles)
# print('\nMost common profile occurs', frequency, 'times:')
# pprint(largest_segment)
