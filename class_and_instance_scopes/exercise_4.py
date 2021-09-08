"""
* Without making any other changes put the `@staticmethod` decorator on the line
  before the `log` method on the `User` class.

* Uncomment the lines of code below, and run this script. Make sure that you
  understand the output you see.

* Now update the `log` method signature so it functions correctly as a static
  method.
"""

from user import User

User.log("This is a log message sent from outside an instance")
