"""Run this script to view the data structures imported for the exercises"""

from pprint import pprint

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


# Uncomment any of the lines below to print out a dictionary to the command line
# ------------------------------------------------------------------------------

# pprint(girls_names_2010)
# pprint(boys_names_2010)
# pprint(boys_popularity_by_decade)
pprint(girls_popularity_by_decade)
