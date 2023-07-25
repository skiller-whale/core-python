
"""
The code below asks the user to enter their year, month and day of birth
(e.g. 1987, 12 and 25), and then prints out their 'fortune' based on an
old English nursery rhyme (called Monday's child).
"""
from fortunes import tell_fortune, ask_for_birthday


"""
Note: For now, you don't need to worry about how the ask_for_birthday and
tell_fortune functions work.

1. Run this file as a python3 script, and enter the year, month and day of your
   birthday (as numbers) in the terminal to get your fortune!

2. Run the file again, and try entering a string (e.g. "March" instead of the
   number 3 for the month). You should see a `ValueError`, because the string
   could not be converted to a number.

3. Add a `try` and `except` block to the `tell_birthday_fortune()` method, so
   that if you enter a non-numeric value for part of the birthday, the code does
   not throw an error, and instead prints a message which says:

  "Invalid Birthday Date!"`

4. Update the `except` block, so that if users enter an invalid date, as well
   as seeing the message, they can try again repeatedly until they have
   entered valid dates.

   (hint: functions in Python can call themselves)
"""

def tell_birthday_fortune():
    birthday = ask_for_birthday()
    tell_fortune(birthday)


tell_birthday_fortune()
