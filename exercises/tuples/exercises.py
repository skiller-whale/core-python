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
2. TUPLES AS KEYS - PART 1
--------------------------

The imported variable `all_profiles` is a large list containing customer profile
dicts (like the ones you've seen in earlier exercises).

Implement the function `count_profiles` which takes a list of profiles and
returns a dictionary where:

* the keys are profile tuples containing: (occupation, age, gender, favourite_shop)
* the values are the number of times that profile type appears in the list.

You should use the `tuple_from_profile` that you wrote in the previous exercise.

For example:

>>> count_profiles([
    {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish', 'name': 'Sharkira'},
    {'occupation': 'Eelectrician', 'age': '10-20', 'gender': 'M', 'favourite_shop': 'Surfways', 'name': 'Eelton John'},
    {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish', 'name': 'Tuna Turner'},
])

Should return:

{
    ('Pilot whale', '30-40', 'F', 'John Lewfish'): 2,
    ('Eelectrician', '10-20', 'M', 'Surfways'): 1,
}

Uncomment the lines of code at the end of this section and test your function.
There should be 8 profiles like ('Whaleway engineer', '50-65', 'F', 'Clamazon')
"""

def count_profiles(profiles):
    counts = {}

    # TODO: complete this function

    return counts


# You can use the following to test your implementation (see above for expected output).
# test_counts = count_profiles([
#     {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish', 'name': 'Sharkira'},
#     {'occupation': 'Eelectrician', 'age': '10-20', 'gender': 'M', 'favourite_shop': 'Surfways', 'name': 'Eelton John'},
#     {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish', 'name': 'Tuna Turner'},
# ])
# print('\n[test] Test `count_profiles`:', test_counts)


# Uncomment when you're done and put these results in your answerbox.
# profile_counts = count_profiles(all_profiles)
# print("\nNumber of Distinct Profiles:", len(profile_counts))
# test_profile = ('Whaleway engineer', '50-65', 'F', 'Clamazon')
# print(f"Profile {test_profile} occurs {profile_counts.get(test_profile, 0)} times")


"""
2. TUPLES AS KEYS - PART 2
--------------------------

Update the function `get_most_common_profile` so that it returns two arguments:

1. The most common profile in terms of (occupation, age, gender, favourite_shop).
2. The number of customers with that profile.

For example:

>>> get_most_common_profile([
    {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish', 'name': 'Sharkira'},
    {'occupation': 'Eelectrician', 'age': '10-20', 'gender': 'M', 'favourite_shop': 'Surfways', 'name': 'Eelton John'},
    {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish', 'name': 'Tuna Turner'},
])

Should return:

('Pilot whale', '30-40', 'F', 'John Lewfish'), 2

You should use the `count_profiles` function you wrote, and the provided
`item_with_largest_value` function to help you.

Uncomment the three lines of code at the bottom to test your functions
"""


# This function is provided to help you - you do not need to change it.
# Note - this is not a particularly efficient implementation, but it is simple.
def item_with_largest_value(d):
    """Return the (key, value) pair corresponding to the largest value in dict `d`"""
    max_value = max(d.values())
    for key, value in d.items():
        if value == max_value:
            return key, value


def get_most_common_profile(profiles):
    # TODO: complete this function
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# most_common_profile, frequency = get_most_common_profile(all_profiles)
# print('\nMost common profile occurs', frequency, 'times:')
# pprint(most_common_profile)
