"""
* Create a subclass of the built-in `str` class called CustomStr.

* Add a method to CustomStr called `is_palindrome` which returns:
  - `True` if the string is the same when reversed.
  - `False` otherwise.

  You can use s[::-1] to reverse the string s.
"""


# <<< DEFINE CustomStr HERE >>>


example_1 = CustomStr(1234321)
example_2 = CustomStr("do geese see god?")
example_3 = CustomStr("redivider")
example_4 = CustomStr(3.3)

print()
for s in [example_1, example_2, example_3, example_4]:
    if s.is_palindrome():
        print(s, "is a palindrome!")
    else:
        print(s, "is NOT a palindrome")
