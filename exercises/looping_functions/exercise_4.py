from utils.example_data import words, word_frequencies

# pylint: disable=pointless-string-statement
"""
UNZIPPING
---------

* Using `words_and_frequencies`, the `filter` function, and unzipping, print out
    the words with a frequency under 5_060_000 (`frequency_threshold`).

HINT: You can use filter(function, collection) to return items from a `collection`
    for which `function(item)` is True
"""

words_and_frequencies = zip(words, word_frequencies)
frequency_threshold = 5_060_000

filtered_pairs = ...
filtered_words = ...

# print("Words with a frequency under 5,000,000:")
# print(*filtered_words)
