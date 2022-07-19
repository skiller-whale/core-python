"""An introduction to nested list comprehensions in Python"""

from pprint import pprint

from example_data import nested_comprehensions_word_list as word_list, nested_comprehensions_words_by_letter as words_by_letter

"""
COMPREHENSIONS WITH MULTIPLE ITERATORS
--------------------------------------

A company sells wooden table tops, which can be cut to a custom (rectangular)
size. The maximum size for each edge is 200cm, and sizes can be cut to the
nearest 1cm. For example, a table top could be requested sized 150cm x 32cm.

The company charges by the amount of wood used, or area of the table top. That
is the requested width * length. Find out the number of possible different areas
that could be requested. Note that some different combinations of dimensions
could result in the same area (2 * 10 is the same as 4 * 5)

1. Uncomment the print statements at the bottom of the section.
2. Update `possible_areas` so that it is a collection containing all of the
   possible areas the company would be able to sell.
3. Update `n_possible_areas` so that it contains the number of distinct values
   in the `possible_areas` collection.

The company has decided it won't sell table tops which "aren't square enough"
where the length and width are more than 50cm apart. So (50 * 90 is fine, but
120 * 180 is not)

4. Update `square_enough_areas` so it contains only the areas which are possible
   for sufficiently 'square' table tops by the definition given above.
5. Update `n_square_enough_areas` so that it contains the number of distinct
   values in the `square_enough_areas` collection.
"""

# Create a list of the possible edge sizes - 1 to 200 (inclusive)
sizes = list(range(1, 201))

possible_areas = ...
n_possible_areas = ...

square_enough_areas = ...
n_square_enough_areas = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# print("It's possible to get", n_possible_areas, "table areas")
# print("It's possible to get", n_square_enough_areas, "'squarish' table areas")


"""
CREATING NESTED LISTS
------------------------------

For this section you will use a list of words, `word_list`. If you wish to look
at the words list, then you can uncomment the `print(word_list)` line to see it
in the output.

Some words in `word_list` are the same as another word except for the first
letter being different. We'll call these 'start_pairs'. For example,
the pairs ['batters', and 'hatters'] or ['clamour' and 'glamour'] are both
start_pairs.

1. Uncomment the assert and print statements in this section
2. Replace the empty list ([]) in the definition of `start_pairs` with a
   nested comprehension so it is a collection containing all of the
   'start pairs' where:
      * the words are more than 5 letters long.
      * the two words are identical EXCEPT for the first letter
   You can choose what type of comprehensions to use (sets, tuples, etc.)
3. Run the script. If your comprehensions are correctly defined then you
   should be able to run it without seeing any errors.
"""

# word_list looks like: ['ability', 'able', 'above', 'abstract', ... , 'zone']
# This print line is just to display word_list, feel free leave it commented.
# print(word_list)

# The start pairs which have more than 5 letters
start_pairs = []

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

for w1, w2 in start_pairs:
    # assert w1[1:] == w2[1:], w1 + " and " + w2 + "are not start pairs"
    # assert len(w1) >= 6, w1 + " is less than 6 letters long"
    pass

# print()
# print("There are", len(start_pairs), "start_pairs with 6 or more letters")
# print(start_pairs)


"""
NESTING COMPREHENSIONS IN COMPREHENSIONS
------------------------------

In this section you'll use a nested comprehension to create a dictionary of
anagrams, where each key is a word, and each value is a list containing all of
the anagrams of the word which occur in word_list.

Note: Anagrams are words which contain EXACTLY the same letters (e.g.
stressed & desserts or elbow & below). desert & dessert are NOT anagrams because
they contain a different number of the letter s.

1. Uncomment the print (and pprint) statements at the bottom of this section
2. Replace the ellipses (...) with a dict comprehension so that anagrams is a
   dict where:
   * Each key is one of the words in `start_words`
   * Each value is a list containing all the anagrams of the key in word_list.

For example, if the start_words were ['seahorse', 'crustacean', 'lobster'], then
anagrams might look like:
{
    'seahorse': ['seashore'],
    'crustacean': [],
    'lobster': ['bolster', 'bolters']
}

HINT: You can tell if two words are anagrams if they are equal once their letters are sorted.
"""

start_words = ['skiller', 'whale', 'dolphin', 'python', 'loops']
anagrams = ...

# print("\nAnagrams:")
# pprint(anagrams)


"""
WORKING WITH NESTED ITERABLES
-----------------------------

countries_by_continent is a list containing four lists, each one containing
countries from a different continent ('Europe', 'North America', 'Africa', 'Asia')

You'll use a list comprehension to transform this list of lists into a
one-dimensional list, `countries` which contains all the countries from each of
the continents.

1. Uncomment the assert and print statements at the bottom of this section
2. Replace the ellipsis (...) with a list comprehension so that
   flattened_countries is a one-dimensional list of country names.
3. Run the script. If your list comprehensions are correctly defined then you
   should be able to run it without seeing any errors. Make sure the list of
   flattened countries looks like what you were expecting.
"""

countries_by_continent = [
    ['Italy', 'Spain', 'Greece'],
    ['US', 'Canada'],
    ['Kenya', 'Tanzania', 'Morocco', 'Tunisia'],
    ['China', 'India', 'Malaysia', 'Bangladesh'],
]

# return a flat country list, like ['Italy', 'Spain', ... , 'Bangladesh']
flattened_countries = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# print("\nCountries list:")
# print(flattened_countries)
#
# assert len(flattened_countries) == 13, "we expected the list to have 13 elements -- did you flatten it correctly?"
# assert type(flattened_countries[0]) == str, "the list has the wrong structure, it should only contain str elements"


"""
WORKING WITH NESTED ITERABLES - EXTENSION
-----------------------------------------

The variable `words_by_letter` is a dictionary containing all of the words in
`word_list` grouped by letter, but not necessarily sorted. For example:
{
    'a': ['ability', 'able', 'above', 'abstract', 'academic', ... , 'az'],
    'b': ['baby', 'background', 'bad', 'bag', 'balance', ... , 'buying'],
    ...
}

Use a nested comprehension to create a list, `first_ten_words_by_letter`, which
contains the alphabetically first 10 words starting with each letter (or all
words starting with that letter if there are fewer than 10).

For example:
['ability', 'able', 'above', 'abstract', 'academic', 'accept', 'accepted', 'accessories', 'accommodation', 'according', 'baby', 'background', ... ]

1. Uncomment the print statements at the bottom of the section
2. Replace the ellipsis (...) with a comprehension which creates a new flat list
   containing the first 10 words starting with each letter of the alphabet.
"""

# Use `words_by_letter` to create first_ten_words_by_letter
first_ten_words_by_letter = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# Make sure that the 'a' words are at the start. The dict containing the words
# cannot be assumed to iterate through the letters in a predictable order.
first_ten_words_by_letter = sorted(first_ten_words_by_letter)

# print("\nFirst ten words starting with each letter")
# pprint(sorted(first_ten_words_by_letter))

# print("The 14th word in the list is:", first_ten_words_by_letter[13])
# print("The 220th word in the list is:", first_ten_words_by_letter[220])


