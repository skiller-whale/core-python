from utils.example_data import words, word_frequencies
from utils.utils import print_rainbow


# pylint: disable=pointless-string-statement
"""
SORTING AND REVERSE SORTING, PART 1
-----------------------------------

In this session you'll be working with a collection of the ~10000 most common English
words. They are not in frequency order, but instead `word_frequencies` is a tuple of the
same length that contains the frequencies.

The function `print_rainbow` accepts any iterator (anything that can be
looped through in a for loop), and prints out the first 7 words.
"""

# * Update `sorted_words` so that it contains the words sorted alphabetically.
sorted_words = ...

print("The first words are:")
print_rainbow(sorted_words)

# * Update `reverse_sorted_words` to be the reverse of `sorted_words``.
reverse_sorted_words = ...

print()
print("The last words are: ")
print_rainbow(reverse_sorted_words)

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert sorted_words[:4] == ['a', 'aa', 'aaa', 'aaron'], \
#     f"Wrong first four sorted_words, {sorted_words[:4]}, should be ['a', 'aa', 'aaa', 'aaron']"
