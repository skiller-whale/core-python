# The pprint function is like print, but displays a dict with one item per line.
from pprint import pprint

# Import dicts containing the popularity of names given to babies in the US in different years.
from example_data import (
    girls_names_2010,
    boys_names_2010,
    girls_names_1960,
    boys_popularity_by_decade,
)

# ------------------------------------------------------------------------------
# girls_names_2010 is a dictionary mapping from lowercase name to the number
# of girls born in 2010 with that name. For example:
# {
#     'sydney': 4328,
#     'camila': 4300,
#     'kaitlyn': 3290,
#     ...
# }
#
# Uncomment the pprint line below and run this script to see what the
# variable girls_names_2010 looks like. It is quite long, so you'll probably
# want to re-comment the line afterwards to keep your display clearer.
# ------------------------------------------------------------------------------

# pprint(girls_names_2010)


"""
INTRODUCTION TO DICTS
---------------------

* Uncomment the print statements in this section.

* Replace both of the "?" below to make the print statements correct.
"""

# print()
# print("There are", "?", "names in girls_names_2010")
# print("There are", "?", "names in boys_names_2010")


"""
ACCESSING AND UPDATING DICT VALUES
----------------------------------

* Uncomment the print statements in this section.

* Replace both of the "?" below to make the print statements correct.
  (remember that all names are in lowercase)

* Add a new line above the print statements that increases the count for boys
  named 'maximus' by 10.

"""

# print()
# print("In 2010 there were", "?", "boys named Maximus")
# print("In 2010 there were", "?", "girls named Terry")

"""
REMOVING ITEMS
--------------

* Uncomment the lines of code in this section

* Replace the "?" so that:
    1. The number of girls named 'leeann' is printed out.
    2. The name 'leeann' is removed from the dict girls_names_2010
"""

# print()
# print("There were", "?", "girls named Leeann")

# print("There are now", len(girls_names_2010), "names in girls_names_2010")
# if 'leeann' in girls_names_2010:
#     print('Leeann has not been removed!')

"""
TESTING FOR MISSING KEYS
------------------------

* Uncomment the print statements in this section, and run the script. You should
  see a KeyError, because no girls were named 'orca' (surprisingly...)

* Add a conditional (if-else statement) so that if test_name is not a key in
  girls_names_2010, the code will print "There were 0 girls named <test_name>"

* Change test_name to 'simona', and 'henry'. For each, run the script to see how
  many girls were born with that name.
"""

test_name = "orca"

# print()
# print("There were", girls_names_2010[test_name], "girls named", test_name)

"""
FETCHING VALUES WITH GET
------------------------

* Uncomment the print statements in the code below, and run the script. You will
  see a KeyError because no boys were named 'dom'.

* Update the code below so that it is more robust to missing names.

  At the moment the code below prints the number of boys with the name equal
  to the variable `name`. Update the code below so that:

  * IF there are no boys with the name `name`, it will print the number of boys
    with the name `fallback_name`.

  * IF there are no boys with either name, it will print the number 0.
"""

name = "dom"
fallback_name = "dominic"

# print()
# print("Number of boys called", name, "(or", fallback_name, "if none):")

# print(boys_names_2010[name])

"""
ITERATING THROUGH A DICT
------------------------

* Uncomment the print statements in the bottom of this section. If you run the
  script now you will see:
    There were 0 girls names starting with J
    There were 0 girls names starting with Q

* Add code in the lines above the `print` statements which will iterate through
  the keys of `girls_names_2010` and update `names_per_letter`. At the end of
  the loop, it should contain the letters of the alphabet as keys, and the number
   of girls names starting with that letter as values. For example:

  {'i': 24, 's': 97, 'e': 62, 'o': 8, 'a': 149, ... , 'y': 7, 'u': 2}

  Remember you can get the first letter of a string called `name` with `name[0]`
"""

names_per_letter = {}  # Initialize an empty dictionary
# you'll update this to include the count for each letter

# <<< YOUR CODE HERE >>>

# print()
# print("There were", names_per_letter.get("j", 0), "girls names starting with J")
# print("There were", names_per_letter.get("q", 0), "girls names starting with Q")

"""
DICT VALUES
-----------

* Uncomment the print statements in this section.

* Update the definitions of the two variables so:

  1. `highest_boys_name_count` is equal to the count of the most popular name for
     boys (i.e. the largest value in `boys_names_2010`)

  2. `second_most_popular_girls_name_count` equal to the count of the second most
     common name for girls (i.e. the second largest value in `girls_names_2010`)

  You won't need to change any of the `print` statements, but might need to use
  the `max` and `sorted` functions.
"""

highest_boys_name_count = "?"
second_most_popular_girls_name_count = "?"

# print()
# print("The most popular boys name in 2010 was given to", highest_boys_name_count, "boys")
# print("The second most popular girls name in 2010 was given to", second_most_popular_girls_name_count, "girls")

"""
ITERATING THROUGH DICT ITEMS
----------------------------

* Uncomment the print statements at the bottom of this section. If you run the
  script now you will see:
    The popularity of Maureen has changed by 0
    The popularity of Madison has changed by 0

* Write code which updates the `popularity_change` dictionary. This should
  contain each name in `girls_names_2010` as a key, with the value equal to
  the change in popularity between 1960 and 2010
  (i.e. count in 2010 - count in 1960).

  For this you will need to use the variable `girls_names_1960`.

  * Note: Don't worry about any names in `girls_names_1960` but not in `girls_names_2010` , you can leave these out of `popularity_change`.
  * If a name is missing from `girls_names_1960`, assume it has a count of `0`.

"""

# Initialize a dictionary containing the count of each letter
popularity_change = {}

# Write code here which iterates through girls_names_2010.items(), and adds
# each name as a key to change_in_popularity. The corresponding value should be
# the difference between the number of girls given the name in 2010 and the
# number given the name in 1960 (from girls_names_1960).
#
# So if there were 47 girls called hilda in 2010, and 458 in 1960, then the
# popularity_change['hilda'] should equal -411  (47 - 458)

# <<< YOUR CODE HERE >>>

# print()
# print("The popularity of Maureen has changed by", popularity_change.get('maureen', 0))
# print("The popularity of Madison has changed by", popularity_change.get('madison', 0))

"""
NESTED DICTS
------------

This section uses the variable `boys_popularity_by_decade`, which looks like this:

    {
        1960: {'david': 85931, 'michael': 84206, 'james': 7687, ...},
        1970: {'henry': 15261, 'tim': 1821, ...},
        ...
    }

* Uncomment the `print` statements. Run the script and make sure you see:

  In 1970, there were ? boys born named Uriel

* Replace the `?` with an expression that will return the number of boys named
  Uriel born in 1970, and run the script again. The last line of output should read:

  In 1970, there were 31 boys born named Uriel

* Add some code that will print out the number of boys called 'Ethan' each decade.
  Your output should look something like the below, but with the correct numbers:

  In 1960 there were 1000 boys born named Ethan
  In 1970 there were 1000 boys born named Ethan
  In 1980 there were 1000 boys born named Ethan
  ...
"""

# print()
# print("In 1970, there were", "?", "boys born named Uriel")

# Add code to print the number of baby boys born called Ethan each decade e.g.
# "In 1960 there were 1000 boys born named Ethan"
# "In 1970 there were 1000 boys born named Ethan"
# etc.

# <<< YOUR CODE HERE >>>
