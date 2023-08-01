from utils.example_data import words, word_frequencies
from utils.utils import is_anagram

# pylint: disable=pointless-string-statement, consider-using-enumerate
"""
COMBINING ITERABLES WITH ZIP
----------------------------

This code searches for anagrams of the word 'post', and prints them, along with
their frequency on the web.

`word_frequencies` is a list of word frequencies for each word in `words`.

* Update the code so that it uses `zip` instead.

* Uncomment the assert statements to check your answers.
"""

search_word = "post"
anagrams = []

for index in range(len(words)):
    word = words[index]
    if is_anagram(word, search_word):
        # Append word to list of anagrams
        anagrams.append({
            'word': word,
            'frequency': word_frequencies[index]
        })
        
for anagram in anagrams:
    word, frequency = anagram['word'], anagram['frequency']
    print(word, "is in `words` and occurs", frequency, "times")

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert list(anagrams[0].values()) == ['spot', 26750929], \
#     f"anagrams[0] is wrong! It's {list(anagrams[0].values())}, should be ['spot', 26750929]"
# assert list(anagrams[-1].values()) == ['tops', 11771127], \
#     f"anagrams[-1] is wrong! It's {list(anagrams[-1].values())}, should be ['tops', 11771127]"
