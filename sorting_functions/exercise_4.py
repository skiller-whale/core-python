from utils.example_data import words, word_frequencies
from utils.utils import print_rainbow
from operator import itemgetter

# pylint: disable=pointless-string-statement
"""
COMBINING ZIP AND SORTED
------------------------

`word_frequencies` contains the frequencies of words for each word in words.

* Update `sorted_words_and_frequencies` so that it contains a list of
    `(word, word_frequency)`, sorted by word frequency in descending order.

[('most popular word', 12345), ('next most popular word', 12241), ... ]

HINT: You can use `zip` together with `sorted`.
"""

sorted_words_and_frequencies = ...

print("Most common words on the English web and their frequencies:")
print_rainbow(sorted_words_and_frequencies)

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert sorted_words_and_frequencies[:2] == [('the', 23135851162), ('of', 13151942776)], \
#     f"Wrong first two sorted_words_and_frequencies, {sorted_words_and_frequencies[:2]}," + \
#         "should be [('the', 23135851162), ('of', 13151942776)]"
