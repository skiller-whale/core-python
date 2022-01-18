import datetime
from example_data import boys_names


"""
1. HIGHER ORDER FUNCTIONS
-------------------------

1. Write a function called run_n_times, which can be used to call a function
   multiple times. Both the function, and the number of times to run the
   function should be received as arguments.

2. Use run_n_times to run print_hello 3 times, and display_time 10 times.
"""

# TODO: Define the run_n_times function here.


def print_hello():
    print("Hello")


def display_time():
    print("Current Time:", datetime.datetime.now())


# TODO: Use run_n_times to call print_hello 3 times and display_time 10 times.



"""
2. BUILT-IN HIGHER ORDER FUNCTIONS
----------------------------------

1. Use the built-in higher order functions to complete the definitions below,
   to replace the three '...' (ellipses).

  * long_names: should be a list including all boys_names with more than 10 letters.
  * begins_with_x: should be a list of all boys_names that begin with x
  * shortest_name: should be the shortest name (or joint shortest) in the boys_names list.

2. Change the `if False` to `if True` near the bottom of this section to check
   your output looks right.
"""

def longer_than_ten(name):
    """Should return True if name is longer than 10 letters long"""
    return len(name) > 10

def begins_with_x(name):
    """Should return True if name starts with 'X'"""
    return name[0] in {'x', 'X'}


long_names = ...     # TODO: Make this a list of names > 10 letter long
x_names = ...        # TODO: Make this a list of all names starting with X
shortest_name = ...  # TODO: Make this the (joint) shortest name


# TODO: Change this False to True
if False:
    print("\nLong Names:")
    for name in long_names:
        print("*", name)

    print("\nNames Starting with X:")
    for name in x_names:
        print("*", name)

    print("\nThe Shortest Name is:")
    print("*", shortest_name)
    print()


"""
3. LAMBDA FUNCTIONS
-------------------

1. Use run_n_times with a lambda expression to print out "Hi There" 4 times.

2. Now, use lambda functions where appropriate to calculate the three new
   variables below (longest_name, q_names, and palindromic_names).

3. Change the `if False` near the bottom of this section to `if True` to check
   your output.
"""

# TODO: Use the run_n_times function to print out "Hi There" 5 times.



# TODO: This should be the (joint) longest name
longest_name = ...

# TODO: This should be a list of all names starting with 'Q'
q_names = ...

# TODO: This should be this the list of all names that are the same forwards
# and backwards, ignoring capitalisation (s[::-1] will reverse the string s)
palindromic_names = ...

# TODO: Change this False to True to check your results
if False:
    print("\nThe Longest Name is:")
    print("*", longest_name)

    print("\nQ Names:")
    for name in q_names:
        print("*", name)

    print("\nPalindromic Names:")
    for name in palindromic_names:
        print("*", name)
    print()
