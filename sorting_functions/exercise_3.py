from utils.example_data import words, word_frequencies
from utils.utils import print_rainbow


# pylint: disable=pointless-string-statement
"""
SORTING ON MULTIPLE CRITERIA
----------------------------

* Sort words in `longest_words_alphabetical` by lengths in _descending_ order.
   Ties should be decided alphabetically in ascending order
   (words of the same length should be sorted alphabetically).

For example: ["krill", "shark", "shoal" "whale", "fish", "cod"]
"""

longest_words_alphabetical = ...

print("The longest words (with ties decided alphabetically) are:")
print_rainbow(longest_words_alphabetical)

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert longest_words_alphabetical[:2] == ['telecommunications', 'characterization'], \
#     f"Wrong first two longest_words_alphabetical, {longest_words_alphabetical[:2]}," + \
#         "should be ['telecommunications', 'characterization']"
