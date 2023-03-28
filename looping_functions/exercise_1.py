from utils.example_data import words, word_frequencies
from utils.utils import print_rainbow

# pylint: disable=pointless-string-statement
"""
REVERSED
---------

In this session you'll be working with a collection of the ~10000 most common English
words. They are not in frequency order, but instead `word_frequencies` is a tuple of the
same length that contains the frequencies.

The function `print_rainbow(items)` prints the first 7 elements in `items`
    with a different color for each item.
"""

# * Print the first 10 elements of `words` and `word_frequencies`.
print(...)

# * Using `reversed`, update the `print_rainbow` statement, so that it prints out
#   the words in the common words list, but in reverse order.

print('The last seven of the most "common words" on the English web:')
print_rainbow(...)
