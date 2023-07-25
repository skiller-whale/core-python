PUN_WORDS = [
    'skill',
    'whale',
    'fin',
    'fish',
    'swim',
    'orca',
    'shark',
]


def capitalize_puns(name):
    """Capitalize 'pun' components in name and make the rest lowercase.

    Example usage:
    >>> capitalize_puns('Mark Whaleburg')
    'mark WHALEburg'
    """
    name = name.lower()
    for pun in PUN_WORDS:
        name = name.replace(pun, pun.upper())
    return name


def create_greeting(name):
    """Create a greeting string addressed to the input name

    Puns in the name will be capitalized, and a greeting word prepended.
    """
    display_name = capitalize_puns(name)
    greeting_word = "Hi"
    return greeting_word + " " + display_name


"""
IMPORTING WITH AN ALIAS
-----------------------

* Import the `create_greeting` function from `useful_functions` with an alias,
so its name doesn't clash with the `create_greeting` in this module.
* Call this function in place of the hardcoded `"Hi" above.
"""


"""
IMPORTING VS RUNNING AS A SCRIPT
--------------------------------

* Uncomment the first print statement below to print out the value of __name__.
  This will be different depending on whether greetings is run as a script, or
  imported as a module.

* Uncomment the remaining 3 lines of code, and add code that means they only
  run when `greetings.py` is run as a script. Run both `greetings.py` and
  `exercises.py` as scripts and verify that the greeting to Alec Baldfin is only
  displayed when `greetings.py` is run as a script.
"""

# print("\nThe greetings module has the __name__:", __name__)

# print("Running greetings.py as a script")
# example_name = "Alec Baldfin"
# print(create_greeting(example_name))
