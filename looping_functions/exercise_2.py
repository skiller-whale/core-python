from utils.example_data import words
from utils.utils import is_anagram

# pylint: disable=pointless-string-statement
"""
ENUMERATE
---------

The code below iterates through all the words in `words`, finds anagrams
of "loop" and prints them out, along with their position in the tuple.

* Refactor this code, so that instead of looping through the indices and looking
    up the words, it uses enumerate to make the code tidier.

* Change the search_word to 'whale'. How many anagrams of 'whale' are there?

"""

search_word = 'loop'
print("Anagrams of", search_word, "...")

for index in range(len(words)):
    word = words[index]
    if is_anagram(word, search_word):
        print(word, "is in `words` at position", index)

"""
ENUMERATE, PART 2
---------

* Using enumerate, add code below to create a unique id for each word in `words`.
    The ids should start at 1. Store them in a dict with words as keys and
    ids as values.

* Uncomment the assert statements below to check your code.

"""

word_id_dict = {}

# assert word_id_dict['killer'] == 6929, \
#     f"Id for 'killer' incorrect, it's {word_id_dict['killer']}, should be 6929."
# assert word_id_dict['whale'] == 4954, \
#     f"Id for 'killer' incorrect, it's {word_id_dict['whale']}, should be 4954."
