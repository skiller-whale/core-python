"""
Without changing the function itself, update the call to `print_details`,
replacing `...` with the necessary arguments so that when the code runs,
it prints the output:

  My name is Skiller Whale
  I am 1 year old
  I am friends with:
  * Fin Diesel
  * Whaleiam Shakespeare
  My favourite island is Majorca
  My favourite music is orcastral
  My favourite flower is the orcaid
"""

# Do not edit this function
def print_details(name, *friends, age=1, **favourites):
    print("My name is", name)
    years_string = "year" if age == 1 else "years"
    print("I am", age, years_string, "old")
    print("I am friends with:")
    for friend in friends:
        print("*", friend)

    for key, value in favourites.items():
        print("My favourite", key, "is", value)


# TODO: Update this function call only
print_details(...)
