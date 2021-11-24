def remove_extra_spaces(s):
    """Remove additional spaces from a string

    Return a string where multiple spaces are all replaced with single spaces,
    and whitespace is trimmed from the ends of the string.

    Example usage:
    >>> remove_extra_spaces('  Skiller    Whale ')
    'Skiller Whale'

    Note: This could be done more neatly using Python's regular expression
    library `re`. If you want to have a go at rewriting this function with `re`
    then it will be good practice at exploring one of Python's more useful
    packages.
    """
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s.strip()


GREETING_WORDS = [
    'Hi there',
    'Hello',
    'Greetings',
    'Ciao',
]


def create_greeting(*args, **kwargs):
    """Returns a greeting word from the set of `GREETING_WORDS`

    *args and **kwargs are permitted here so the function does not error if it
    is called with arguments. It would be very unusual for this to be useful in
    real code, but in this case it's useful for didactic purposes.
    """
    # TODO: Randomly select one of the GREETING_WORDS instead of "Hey"
    return "Hey"


if __name__ == "__main__":
    print("Example greetings:")
    selected_greetings = [create_greeting() for _ in range(10)]
    print(selected_greetings)

    # Ensure that only members of the GREETING_WORDS set are returned
    unexpected_greetings = set(selected_greetings) - set(GREETING_WORDS)
    assert not unexpected_greetings, \
        "Unexpected greetings returned: " + str(unexpected_greetings)
