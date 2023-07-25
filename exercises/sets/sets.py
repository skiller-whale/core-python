import time

# A set containing several english words
from example_data import words


"""
INTRODUCTION TO SETS
--------------------

This section looks at a set of words, `words`, and tries to find out some basic
properties of the words. If you wish to look at the words set, then you can
uncomment the print(words) line and run this script.

Replace the Ellipses (...) in the variable definitions below, so the code will
print out the expected values instead.
"""

# This line is just to show you what words looks like, feel free to recomment it
# print(words)


number_of_words = ...   # The number of items in the `words` set
first_word = ...        # The alphabetically first word in the set
third_last_word = ...   # The alphabetically third last word in the set

# This variable should be True if "skiller" is in `words` and False otherwise
skiller_is_in_words = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE >>>

print()
print("There are", number_of_words, "words in the `words` set")
print("The alphabetically first word is", first_word)
print("The alphabetically third last word is", third_last_word)
if skiller_is_in_words:
    print("'skiller' is in words")
else:
    print("'skiller' is not in words")


"""
UNIQUENESS
----------

Replace the pass statement in the for loop below, so that it prints each of the
words in the `words` set that use the same set of letters as the word 'skiller'.

Note: This is different to finding anagrams, since one letter can be used
multiple times. "hoop" and "hop" are not anagrams, but they do use the same set
of letters: {'h', 'o', 'p'}
"""

# print()
# print("The following words use the same set of letters as 'skiller':")

for word in words:
    pass


"""
EFFICIENT LOOKUP
----------------

Uncomment the print statements and run the script. You should be able to see
how quickly the membership (in) function runs for lists and tuples.

Add code that will test how quickly the membership function performs for
a set containing the same items as long_list and long_tuple. Update the print
statement so the correct number of milliseconds is displayed instead of the
Ellipsis (...).
"""

def time_membership_test(collection):
    """Time how long it takes for 5000 membership checks of collection
    This function takes a collection (list, tuple, set, etc)
    """
    start = time.time()
    for _ in range(5000):
        -1 in collection

    duration = time.time() - start
    return round(duration * 1000, 1)


# Create these in the REPL if you want to take a look at them
long_list = list(range(10000))  # list containing all numbers from 0 to 9999
long_tuple = tuple(long_list)  # tuple containing all numbers from 0 to 9999

# print()
# print("Time for list lookup:", time_membership_test(long_list), "milliseconds")
# print("Time for tuple lookup:", time_membership_test(long_tuple), "milliseconds")
# print("Time for set lookup:", ..., "milliseconds")


"""
ADDING VALUES TO A SET
----------------------

Update the code below so that the print statement will display the number of
unique two-letter patterns at the start of a word in the `words` set.

To do this, replace `pass` in the `for` loop with code that will add all of the
unqiue two-letter starts of words to the set `two_letter_starts`.

For example, the start of "whale" is "wh", and the start of "who" is also "wh",
so these two words would only add the string "wh" to `two_letter_starts`.
"""

two_letter_starts = set()

for word in words:
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("There are", len(two_letter_starts), "unique two letter word starts")


"""
REMOVING VALUES FROM A SET
--------------------------

Implement the function `remove_items` so that it removes all of the elements in
`items_to_remove` from the set `s` using the `remove()` method. If
`items_to_remove` contains additional elements which aren't in `s` then they
can be ignored.

Implement the function `discard_items` to do the same as `remove_items`, but
use `discard()` instead of `remove()`. This should be a little bit simpler
than the `remove_items` function.
"""

def remove_items(s, items_to_remove):
    """Remove all of the elements in items_to_remove from the set s

    This should be done using s.remove()
    """
    # <<< YOUR CODE HERE - use the remove method only >>>
    pass


def discard_items(s, items_to_remove):
    """Remove all of the elements in items_to_remove from the set s

    This should be done using s.discard()
    """
    # <<< YOUR CODE HERE - use the discard method only  >>>
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

test_set_1 = {'a', 'b', 'c', 'd'}
remove_items(test_set_1, {'b', 'd', 'e'})

test_set_2 = {'m', 'n', 'o', 'p'}
discard_items(test_set_2, {'m', 'p', 'q'})

# print()
# assert {'a', 'c'} == test_set_1, f"remove_items failed, test_set_1 is {test_set_1} instead of {{'a', 'c'}}"
# print("remove_items is working as expected")
# assert {'n', 'o'} == test_set_2, f"discard_items failed, test_set_2 is {test_set_2} instead of {{'n', 'o'}}"
# print("discard_items is working as expected")
