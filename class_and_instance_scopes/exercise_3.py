"""
* Identify the methods in the `User` class which do not need access to the
  instance, and convert them to `classmethod`s.

* Add a new classmethod called `create_customer`, which takes one argument,
  `name`, and returns a new `User` with the 'customer' role, and the given name.

* Uncomment the lines of code below
"""

from user import User

new_customer = User.create_customer("John Belugashi")
