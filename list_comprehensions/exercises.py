"""An introduction to list comprehensions in Python"""

from example_data import word_list

"""
MAPPING VALUES
--------------

For this section you will use a list of words, `word_list`, and perform some
transformations on this list using list comprehensions

If you wish to look at the words list, then you can uncomment the
`print(word_list)` line to see it in the output.


At the moment, several new lists are created from `word_list` using `for` loops:

* `word_lengths_from_loop` - a list of the length of each word in word_list.
* `outer_letters_from_loop` - a list containing the first and last letter of
                              each word in `word_list` as a string.
* `just_ones_from_loop` - a list the same length as `word_list` where every item
                          is the number 1.

You will be creating equivalent lists, but doing so using list comprehensions
instead of for loops. There are then some lines at the end of the section which
check that your result is the same.

1. Uncomment the assert and print statements at the bottom of this section
2. Replace each of the ellipses (...) in the definitions of `word_lengths`,
   `outer_letters` and `just_ones` with a list comprehension so that these
   variables end up as lists which are the same as their `_from_loop` equivalent.
3. Run the script. If your list comprehensions are correctly defined then you
   should be able to run it without seeing any errors.
"""

# word list looks like: ['ability', 'able', 'above', 'abstract', ... , 'zone']
# This print line is just to display word_list, feel free leave it commented.
print(word_list)


# Get a list of the lengths of all of the words: [7, 4, 5, 8, ... , 4]
word_lengths_from_loop = []
for word in word_list:
    word_length = len(word)
    word_lengths_from_loop.append(word_length)


# A list of the outer letters of all the words (first and last letter):
# e.g. ['ay', 'ae', 'ae', 'at', ... , 'ze']
outer_letters_from_loop = []
for word in word_list:
    word_outer_letters = word[0] + word[-1]
    outer_letters_from_loop.append(word_outer_letters)


# Get a list the same length as `word_list`, where each item equals `1`
# Note: By convention iteration variables are named `_` if they aren't used
# [1, 1, 1, 1, 1, ... , 1]
just_ones_from_loop = []
for _ in word_list:
    just_ones_from_loop.append(1)


# <<< CHANGE THE LINES BELOW HERE  - replace ... with list comprehensions >>>

word_lengths = ...
outer_letters = ...
just_ones = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# print()
# assert word_lengths_from_loop == word_lengths, \
#     "word_lengths does not match word_lengths_from_loop"
# print("word_lengths list comprehension is correct!")
# assert outer_letters_from_loop == outer_letters, \
#     "outer_letters does not match outer_letters_from_loop"
# print("outer_letters list comprehension is correct!")
# assert just_ones_from_loop == just_ones, \
#     "just_ones does not match just_ones_from_loop"
# print("just_ones list comprehension is correct!")


"""
MAPPING VALUES EXTENSION - Only do this section if you finish the above one

The variable `number_of_vowels_from_loop` below is a list which counts the
number of vowels in each word in `word_list`.

1. Uncomment the print and assert statements at the bottom of the section
2. Replace the ellipsis `...` with a list comprehension which results in
   `number_of_vowels` being equal to `number_of_vowels_from_loop`

Note: You may well need to write a separate function (e.g. `count_vowels`)
to use in the list comprehension.
"""

# Get a list of the number of vowels (a, e, i, o, u) in each word in `word_list`
# [3, 2, 3, 2, ... , 2]
number_of_vowels_from_loop = []
for word in word_list:
    count = 0
    for letter in word:
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    number_of_vowels_from_loop.append(count)


# <<< CHANGE THE LINES BELOW HERE  - replace ... with a list comprehension >>>
# Note: You will probably also want to define a separate function

number_of_vowels = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# assert number_of_vowels_from_loop == number_of_vowels, \
#     "number_of_vowels does not match number_of_vowels_from_loop"
# print("number_of_vowels list comprehension is correct!")


"""
SCOPING OF ITERATION VARIABLES
------------------------------

The code below takes a variable, `word`, and finds the number of words in
`word_list` which start with the same letter. To do this, it iterates through
word_list, and creates a new list where each element is `True` or `False`.

However, there is a bug in the code which you
can fix by using a list comprehension instead (there are other ways to fix the
bug, but try to do it using a list comprehension).

1. Uncomment the print and assert statements at the bottom of the section. If
   you run the script now you should see some unexpected output.
2. This is being caused by the iteration variable, `word`, in the for loop.
   Replace the for loop with the line:

   `starts_with_same_letter = [word[0] == first_letter for word in word_list]`

   Note: Make sure you actually replace the `for` loop (or comment it out). If
   you just add the list comprehension below then you'll still get the error.
3. Run your script again. You should now see that the variable `word` is still
   equal to its starting value, even though the list comprehension is doing the
   same operations as the for loop
"""

# Define a variable, `word` which our program will use later
# (if you're interested, bombinate means "to make a humming or buzzing noise")
word = "bombinate"
first_letter = word[0]

# <<< CHANGE THE CODE BELOW HERE  >>>

# Create a list of booleans where each item is `True` if the corresponding word
# in word_list starts with same letter as `word`, and `False` otherwise
starts_with_same_letter = []
for word in word_list:
    starts_with_same_letter.append(word[0] == first_letter)

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# Note: You can use the `sum` function on a list of numbers or booleans. True is
# treated as 1, and False as 0, so e.g. `sum([True, True, False, True]) == 3`
count_with_same_letter = sum(starts_with_same_letter)

# print()
# print("My favourite word is", word)
# print("It starts with the letter", first_letter)
# print(count_with_same_letter, "words in word_list start with the same letter")
# assert word == "bombinate", \
#     "Oops... You've overwritten 'bombinate' with '" + word + "'!"

"""
THE TERNARY OPERATOR
--------------------

Replace the ellipsis (...) below with a list comprehension which contains a
modified version of each of the words in `word_list`. This list should be
created so:

* Every word shorter than 7 letters has the `_short` suffix.
* Every word with 7 or more letters has the `_long` suffix.

So 'skiller' goes to 'skiller_long', and 'python' goes to 'python_short'.

Uncomment the print statements at the bottom of the section, and run the script.
"""

modified_words = ...

# print()
# print('First modified word:', modified_words[0])
# print('Last modified word:', modified_words[-1])
# print('1475th modified word:', modified_words[1474])


"""
FILTERING VALUES
----------------

In the code below use list comprehensions to create three lists that are subsets
of `word_list`.

* `list_a` - should contain all the words in `word_list` that are 3 letters long
* `list_b` - should contain all the words in `word_list` that have more than
             8 letters, and end with the letter 'c'
* `list_c` - should contain all the words in `word_list` that have fewer than
             5 letters, start with the letter 'a', and contain the letter 't'
             (e.g. 'arts')

"""

list_a = ...
list_b = ...
list_c = ...

# print()
# print("There are", len(list_a), "three letter words in word_list")
# print("There are", len(list_b), "words longer than 8 letters, which end with c:")
# print(list_b)
# print("There are", len(list_c),
#       "words shorter than 5 letters, which start with a, and contain t:")
# print(list_c)


"""
COMBINING MAPPING AND FILTERING
-------------------------------

Replace the ellipsis in the code below with a single list comprehension so that
`reversed_long_words` contains reversed versions of all the words in `word_list`
that are more than 13 letters long.

So for example, if `listcomprehension` were in `word_list`, then
`reversed_long_words` would contain the string `'noisneherpmoctsil'.

NOTE: A string can be reversed using slicing:

    >>> a_string = 'hello'
    >>> a_string[::-1]
    ... 'olleh'

Uncomment the print statements, and make sure that your script runs successfully
and that the result looks plausible

"""

reversed_long_words = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("There are", len(reversed_long_words), "words longer than 13 letters")
# print("The alphabetically last reversed long word is", max(reversed_long_words))
