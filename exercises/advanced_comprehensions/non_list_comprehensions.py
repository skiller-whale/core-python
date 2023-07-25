"""An introduction to non-list comprehensions in Python"""

from example_data import non_list_comprehensions_word_list as word_list


"""
For these section you will use a list of words, `word_list`, and perform some
transformations on this list using list comprehensions

If you wish to look at the words list, then you can uncomment the
`print(word_list)` line to see it in the output.

"""

# print(word_list)


"""
SET AND TUPLE COMPREHENSIONS
--------------------

1. Replace the first ellipsis (...) below, with a set comprehension, which iterates
through `word_list`, and includes the first three letters for all words
starting with `k`.

For example, if word_list were `['keyhole', 'key', 'door', 'keychain', 'kayak']`
then `k_word_starts` would be `{'key', 'kay'}`


2. Replace the second ellipsis (...) below with a tuple comprehension, which iterates
through code_string, so that `no_vowels` is a tuple containing the characters
of code_string which are not vowels (aeiou), or spaces.

The str.lower() method might come in useful for this: "A".lower() == "a".
"""

# The set of three letter word starts beginning with k
k_word_starts = ...


code_string = "I aSk yoU all herE - Why hUEl!"

# Tuple containing all characters from code_string except vowels or spaces
no_vowels = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print("There are", len(k_word_starts), "three letter word starts beginning with k:")
# print(k_word_starts)


# print()
# print("Encoded message:", code_string)
# print("Decoded characters:", no_vowels)

# The str.join method can be used to convert a list of characters back to a str
# If you'd like to understand how this works, check out the python docs online!
# print("Decoded message", ''.join(no_vowels))


"""
DICT COMPREHENSIONS
------------------

Replace the ellipsis (...) below, with a dict comprehension, which iterates
through `word_list`, and creates a dict which has a key of a word, and a value
of the length of that word, only for each word beginning with k in word_list.

For example, if word_list were `['keyhole', 'key', 'door', 'keychain', 'kayak']`
then `k_word_lengths` would be `{'keyhole': 7, 'key': 3, 'keychain': 8, 'kayak': 5}`
"""

# The dictionary of words beginning with k and their lengths
k_word_lengths = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("The length of each word beginning with k is:")
# print(k_word_lengths)


"""
USING A DICTIONARY ITERABLE
------------------

Replace the ellipsis (...) below, with a dict comprehension, which iterates
through the keys and values of the `k_word_lengths` dict and creates a new dict
which has the same keys and values, but only for words that are 7 letters or
longer.

For example, if `k_word_lengths` were `{'keyhole': 7, 'key': 3, 'keychain': 8, 'kayak': 5}`
then `long_k_words` would be `{'keyhole': 7, 'keychain': 8}`
"""

# The dictionary of words beginning with k and their lengths, only for words of
# 7 letters or more.
long_k_words = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("The length of each long word beginning with k is:")
# print(long_k_words)
