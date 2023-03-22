from utils.example_data import words, word_frequencies
from utils.utils import is_anagram

# pylint: disable=pointless-string-statement
"""
COMBINING ITERABLES WITH ZIP
----------------------------

This code searches for anagrams of the word 'post', and prints them, along with
their frequency on the web.

* Uncomment the two print statements in the code in this section.

* Update the code so that it uses `zip` instead.

"""

search_word = "post"

for index in range(len(words)):
    word = words[index]
    if is_anagram(word, search_word):
        frequency = word_frequencies[index]
        print(word, "is in `words` and occurs", frequency, "times")

