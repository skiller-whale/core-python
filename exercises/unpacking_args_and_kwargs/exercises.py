"""
1. UNPACKING COLLECTIONS
------------------------

In get_name_components, simplify the assignment of the variables first_name,
last_name and middle_names using unpacking.
"""

def get_name_components(full_name):
    """Takes a name and returns first name, last name and a list of middle names"""
    names = full_name.split(' ')  # Split names into a list of strings

    # TODO Simplify this code using unpacking
    first_name = names[0]
    last_name = names[-1]
    middle_names = names[1:-1]
    return first_name, last_name, middle_names



first, last, middle = get_name_components("Johann Seabasstian Bach")
print('First name:', first)
print('Surname:', last)
print('Middle names:', middle)



"""
2. *args
--------

Update the function `longest_name` so that instead of taking two names, it can
take any number of names as arguments and will return the longest name.
"""


def longest_name(name_1, name_2):
    if len(name_1) > len(name_2):
        return name_1
    else:
        return name_2

# print()
# print("Longest name of two:", longest_name('dominique', 'quinton'))
# print("Longest name of four:", longest_name('dominic', 'quinton', 'humberto', 'guillermo'))



"""
3. **kwargs
-----------

Update the function `most_popular_name` so that instead of taking two values,
it can take any number of name popularities as keyword arguments. The name
should be the keyword, and the popularity the value.

The function should then return the most popular name.
"""

def most_popular_name(joaquin, monique):
    """each argument is the popularity of the name"""
    if joaquin >= monique:
        return 'joaquin'
    else:
        return 'monique'


# print()
# print("Most popular name of two:", most_popular_name(joaquin=23, monique=42))
# print("Most popular name of four:", most_popular_name(dominique=32, quinton=45, humberto=91, guillermo=3))


"""
4. USING COLLECTIONS AS ARGUMENTS
---------------------------------

The `fancy_print` function should behave exactly the same way as `print`, but
print additional lines above and below the normal printed output.

Update the fancy_print function, by:

1. Replacing the TODO in the signature so fancy_print can accept ANY arguments
2. Updating the central call to print, so it receives the exact same arguments
   that were passed into fancy_print.
"""

def fancy_print(TODO):
    print("\n-----------------------------------------\n>>>")
    print(">>>   ", end="")

    # TODO Update this call to print, replacing the ...
    print(...)

    print(">>>\n-----------------------------------------")


# Don't change any of the print statements below here, except to uncomment them

# print()
# print("Hello", "from", "Skiller Whale", sep=' | ', end='!!!\n')
# fancy_print("Hello", "from", "Skiller Whale", sep=' | ', end='!!!\n')
