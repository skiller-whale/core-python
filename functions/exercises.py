# This imports some data into your script - you can ignore this (but don't delete it)
# -----------------------------------------------------------------------------------
# Popularities of female and male names in the US over several decades
from example_data import (
    boys_popularity_by_decade,
    girls_popularity_by_decade,
)

girls_names_2010 = girls_popularity_by_decade[2010]
boys_names_2010 = boys_popularity_by_decade[2010]

# boys_popularity_by_decade and girls_popularity_by_decade have the structure:
#
# {
#     1960: {'name 1': 123, 'name 2': 234, ...},
#     1970: {'name 3': 345, 'name 4': 456, ...},
#     ...
# }
#
# If you want to look at these variables in more detail, you can uncomment lines
# at the bottom of `./view_data.py` one at a time, and run the file as a script


"""
PARAMETERS AND ARGUMENTS
------------------------

1. Uncomment the lines starting with print_number_of_names, and run this script.
   You should see a NameError indicating that the function does not exist:

2. Write a function print_number_of_names which expects parameters (in order)
   * name
   * popularities_by_year  (a dictionary with the same structure as girls_popularity_by_decade)
   * year

    When it's called, this function should print the number of people in the
    popularities_by_year dictionary who have the given name in the specified
    year. The printed line should look like:

    "There were <number> girls called <name> in <year>"
"""

# <<< WRITE YOUR FUNCTION HERE >>>

# print_number_of_names('catherine', girls_popularity_by_decade, 2010)
# print_number_of_names('kathryn', girls_popularity_by_decade, 2010)
# print_number_of_names('katharine', girls_popularity_by_decade, 2010)
# print_number_of_names('katherine', girls_popularity_by_decade, 2010)


"""
POSITIONAL AND KEYWORD ARGUMENTS
--------------------------------

1. Uncomment all of the lines of code in this section, and run the script.
   You should see a TypeError.

   If you aren't sure, or can't work out why this TypeError happens, ask the
   trainer for an explanation.

2. Without rearranging any arguments, add as few keywords as possible to
   the function calls below, so that the calls succeed.
"""

# print()
# print_number_of_names('hailey', 2010, girls_popularity_by_decade)
# print_number_of_names(2010, 'hayley', girls_popularity_by_decade)
# print_number_of_names(girls_popularity_by_decade, 'haylee', 2010)
# print_number_of_names('haley', girls_popularity_by_decade, 2010)


"""
DEFAULT ARGUMENT VALUES
-----------------------

1. Edit the `print_number_of_names` function above, by adding some default
   arguments for `year` and `popularities_by_year` that let you simplify all of
   the calls to the function.

2. Update the calls to `print_number_of_names` in the PARAMETERS AND ARGUMENTS
   section so that default argument values are used. None of the output should
   be changed when you run the script.

3. There is still quite a lot of repetition in your code. Create a new function
   called `compare_names`, which expects the parameters:

    * `names`, which is a list of names.
    * `popularity_by_year` which has the default value of `girls_names_2010`
    * `year` which has the default value of `2010`

   This function should loop through names, and call `print_number_of_names`
   for each one.

   Use this new compare_names function to compare the popularity of the
   spellings of 'catherine'. You will need to use the names list defined below:
"""

names = ['catherine', 'kathryn', 'katharine', 'katherine']

# <<< YOUR CODE HERE >>>


"""
RETURNING VALUES
----------------

Two functions are defined below: `most_popular_name` and `least_popular_name`,
each of which takes a {name: count} style dictionary.

1. Uncomment the print statements at the bottom of this section.

2. Write the body of the function `get_extreme_names`, so that it returns the
   least, and most popular names, and the print statements work as intended.

   You will probably want to use the existing functions to make this easier.
"""


def most_popular_name(name_popularities):
    max_count = max(name_popularities.values())
    for name, popularity in name_popularities.items():
        if popularity == max_count:
            return name


def least_popular_name(name_popularities):
    min_count = min(name_popularities.values())
    for name, popularity in name_popularities.items():
        if popularity == min_count:
            return name


def get_extreme_names(name_popularities):
    """Return the most, and least popular names from the name_popularities dictionary"""
    pass  # TODO: Complete this function


# print()
# print("The most popular girls name in 2010 was:", most_popular_name(girls_popularity_by_decade[2010]))
# print("The least popular girls name in 2010 was:", least_popular_name(girls_popularity_by_decade[2010]))

# most_popular, least_popular = get_extreme_names(boys_popularity_by_decade[2010])
# print("The most popular boys name in 2010 was:", most_popular)
# print("The least popular boys name in 2010 was:", least_popular)

"""
MULTIPLE RETURN STATEMENTS
--------------------------

1. Uncomment all the lines of code at the bottom of this section.

2. Update the function `contains_orca`, so that it returns True if `name` contains
   all of the letters from the string "orca", and `False` otherwise.

   HINTS:
     * You can check whether a letter is in a string using e.g. 'o' in some_string
     * Think about what it means if the letter "o" is NOT in the `name` variable.
       The function is much easier to write that way round.

   Run the code, and check that the names you see do contain all of the letters
   from orca!

3. Update the function `contains_word`, so it is a more general version of
   `contains_orca`. This function should:
     * Expect `name` and `word` as two string arguments.
     * Return `True` if all letters from `word` are in `name`.
     * Return `False` otherwise.
"""


def contains_word(name, word):
    pass


# Edit this function so it returns True if name contains all the letters of
# orca, and false otherwise
def contains_orca(name):
    for letter in "orca":
        # TODO: Complete this function
        pass


# print()
# for name in boys_popularity_by_decade[1970]:
#     if contains_orca(name):
#         print(name, "contains the letters from orca")

# print()
# test_word = 'krill'
# for name in boys_popularity_by_decade[1970]:
#     if contains_word(name, test_word):
#         print(name, "contains the letters from", test_word)
