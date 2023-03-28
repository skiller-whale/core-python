def print_rainbow(iterable):
    """prints the first few words out as a rainbow"""
    background_colour = 40
    colours = list(range(31,38))
    iterator = iter(iterable)
    for colour, item in zip(colours, iterator):
        format_string = f'0;{colour};{background_colour}'
        print(f'\x1b[{format_string}m {item} \x1b[0m')
    try:
        next(iterator)
        # If there are still items left, then print '...'
        print(' ...')
    except StopIteration:
        pass


def print_rainbow_plain(iterable):
    """A replacement function in case shells do not support print_rainbow"""
    n_to_print = 7
    iterator = iter(iterable)
    for _ in range(n_to_print):
        print(f" {next(iterator)} ")
    try:
        next(iterator)
        # If there are still items left, then print '...'
        print(' ...')
    except StopIteration:
        pass

def is_anagram(word1, word2):
    "Checks if word1 is an anagram of word2 (case-sensitive)."
    return sorted(word1) == sorted(word2)
