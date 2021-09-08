"""
PART 1. (Check for Duplicate IDs)
-------

There is currently nothing to prevent duplicate user ids, so if you run this
script, you should see the output:

>>> USER LOG:  User 123 - First Duplicate User created with role: employee
>>> USER LOG:  User 123 - Second Duplicate User created with role: employee

* Add a class attribute to `User` called `all_user_ids` which, contains the
  `user_id` for every instance of `User`. You'll need to:
    1. Initialize `all_user_ids` as an empty set, `set()`.
    2. Add a line to the constructor so that when a new `User` is created, its `user_id` is added to `all_user_ids`.

* Run this file again and check you see the output `All User IDs: {123}`.

* Update the `is_unique` method, so that it only returns True if the `user_id`
  hasn't already been used by an existing instance.

* Run the file again, and check that you see a `ValueError` because the user
  id 123 is not unique.

PART 2. (Auto-Generate New IDs)
-------

* Update the constructor for `User` so that `user_id` is an optional argument,
  with a default value of `None`.

* If `user_id is None`, then set the `user_id` attribute to the
  largest id so far + 1.
  E.g. if the largest user id seen so far was `8`, the next `User` initialized
  with no `user_id` specified would have their `user_id` set to `9`.

  You might want to use the `max()` function, which returns the largest number
  in a collection.

* Update the line creating Second Duplicate User, so that id is no longer
  provided as a final argument:

  Run the file again, to check that the second User is successfully created and
  has a `user_id` of `124`.
"""

from user import User


user = User("First Duplicate User", "employee", 123)
user = User("Second Duplicate User", "employee", 123)

if hasattr(User, 'all_user_ids'):
    # This line will only run if the User class has all_user_ids defined
    print("All User IDs:", User.all_user_ids)
