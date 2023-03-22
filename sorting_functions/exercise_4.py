from utils.example_data import words, word_frequencies
from utils.utils import print_rainbow


# pylint: disable=pointless-string-statement
"""
COMBINING ZIP AND SORTED
------------------------

* Update `sorted_words_and_frequencies` so that it contains a list of
    `(word, word_frequency)`, sorted by word frequency in descending order.

[('most popular word', 12345), ('next most popular word', 12241), ... ]

HINT: You can use `zip` together with `sorted`.
"""

sorted_words_and_frequencies = ...

print("Most common words on the English web and their frequencies:")
print_rainbow(sorted_words_and_frequencies)
