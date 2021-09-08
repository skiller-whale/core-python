"""
Add the following class attributes to the `User` class:
  * `ADMIN_ROLE`, with the value `'admin'`
  * `EMPLOYEE_ROLE`, with the value `'employee'`
  * `CUSTOMER_ROLE`, with the value `'customer'`
  * `ALLOWED_ROLES`, which is a `set` containing the three values for the
    other three attributes.

Make sure that each of the strings `'admin'`, `'employee'`, and `'customer'`
only appear once in your class definition.

Using one or more of these class attributes, update the method `is_valid_role`,
so that it only returns `True` if `role` has one of the three allowed values.

Run this script, and ensure that you see an error (`ValueError: Invalid role`)
when you try to create a user with the `'hacker'` role.
"""

from user import User


user_1 = User("Person 1", "admin", 1)
user_2 = User("Person 2", "employee", 2)
user_3 = User("Person 3", "customer", 3)

# This User should not be allowed
user_4 = User("Person 4", "hacker", 4)
