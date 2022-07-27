"""An introduction to reading and writing files"""

import os
from collections import Counter


# Don't worry about this bit for now. The code below gets the absolute path to
# the file you'll need to load, using whichever of '\' or '/' your system uses.

# If you run the Python script from the directory containing `users_log.txt`
# then it would be enough to just set `log_file_path = 'users_log.txt'`

this_file_path = os.path.abspath(__file__)  # e.g. /Users/me/core-python/reading_and_writing_files/reading_and_writing_files.py
file_dir = os.path.dirname(this_file_path)  # e.g. /Users/me/core-python/reading_and_writing_files/
log_file_path = os.path.join(file_dir, 'users_log.txt')  # e.g. /Users/me/core-python/reading_and_writing_files/users_log.txt

print("Log file located at:", log_file_path)


"""
READING TEXT FILES
------------------
The variable `log_file_path` defined above is the path to a text file, which
has been used to log a user name each time a user logs on to Skiller Whale.
Each line of the file contains exactly one name.

* Uncomment the `print` statements in this section
* Add code below which will open the file at `log_file_path` and read the data
  into the variable `all_names`. You'll need to add at least one new line of
  code, and replace the ellipsis (...).
* Update the final `print` statement in this section, so that instead of
  printing `Ellipsis` your code will print the first 60 characters of the
  log file.
"""

all_names = ...

# print()
# print("First 60 characters of the log file:")
# print(...)


"""
READING FILES AS LISTS OF LINES
-------------------------------

Instead of one long string, the contents of this file would be more useful as a
list of names (one for each line of the file).

* Uncomment the `print` statements in this section.

* In the space below, add code to open `log_file_path` and store its contents
  as a list of names in the variable `all_names_list`.

* Update the final `print` statement in this section, so that instead of
  printing `Ellipsis` (...) your code will print the final three names in the
  log file.

  * BONUS: At the moment, these names will all end with a newline character `\n`
    If you have time, then update the code so it will remove these newline
    characters.
    You might want to use the `.strip()` method which removes space characters
    from the start and end of strings. For example:
    >>> '  ringo starfish  \n'.strip()
    'ringo starfish'
"""

all_names_list = ...

# print()
# print("Last 3 names in the log file:")
# print(...)


"""
WRITING FILES
-------------
Now you have a list of all the names from the log file, you can use a Counter
object to find the users who have most often accessed Skiller Whale. This code
is already written out below, with the results placed in the variable
`top_20_users`. You'll want to write this out to a new file.

* Uncomment the lines of code below and run the script to see the value of
  the `top_20_users` variable. Don't worry too much about how the Counter works,
  you won't need to change this code.

* Write the top 20 users to the file located at `frequent_users_path`, so that
  the top 20 users are each written on a separate line.
  * HINT: `top_20_users` is a `list` of `tuple`s, so you'll need to iterate
    through the `list`, and fetch the first element from each `tuple`
    [('name1', count1), ('name2', count2), ('name3' count3), ...]. We only want
    to write the names to the file.

  * BONUS: If you complete this, then update your code so that the count for
    each name will also be written to file. Each line in the file should include
    the name, a colon (:) followed by a space, and the count, for example:
    ```
    barracuda obama: 123
    ```
"""

# user_counts = Counter(all_names_list)
# top_20_users = user_counts.most_common(20)

# print()
# print("The Top 20 Users are:")
# print(top_20_users)

# # Create the path that the new file will be saved to
# frequent_users_path = os.path.join(file_dir, 'most_frequent_users.txt')
# print("Saving user count to:", frequent_users_path)

# <<< WRITE CODE BELOW THIS LINE >>>


"""
WORKING WITH MULTIPLE FILES
---------------------------
In `users_log.txt`, all of the names are written in lowercase. Create a copy of
this file, but where all names are title-case. For example, the file:

-------------------
justfin swimberlake
tuna turner
-------------------

would be converted to:

-------------------
Justfin Swimberlake
Tuna Turner
-------------------

* Uncomment the print statements below

* Add code which will read the `users_log.txt` file, capitalize each name,
  and write it to a new line in the `updated_users_log.txt` file.

  * To convert a string to its title form, use the `.title()` function:
    >>> 'ringo starfish'.title()
    'Ringo Starfish'

  * The file path to save to is stored in the variable `updated_log_file_path`

  * The written file should look the same as `most_frequent_users.txt`, except
    that all the names should be capitalized
"""

updated_log_file_path = os.path.join(file_dir, 'updated_users_log.txt')

# print()
# print("Saving updated users log to:", updated_log_file_path)

# <<< WRITE CODE BELOW THIS LINE >>>
