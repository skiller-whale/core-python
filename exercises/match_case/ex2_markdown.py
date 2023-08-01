from utils.example_data import (
    MARKDOWN_PATH,
    EXPECTED_LEVEL_2_HEADERS,
    EXPECTED_TITLECASE_MARKDOWN
)

# pylint: disable=pointless-string-statement
"""
EXERCISE 2, Part 1: PARSING MARKDOWN FILES
------------------------

* Using `match`-`case`, implement `extract_level_2_headers`
    so that it extracts level 2 headers from a markdown file.
    Level 2 headers are on lines starting with `## `:

```markdown
# This is a level 1 header
This is some text.

## This is a level 2 header
* This is a list.

## This is another level 2 header
<!-- this is a comment -->
```

HINT: To convert a list of strings back to a string you can use `' '.join(list_of_strings)`.
"""

def extract_level_2_headers(markdown_path):
    """Extracts level 2 headers from a markdown file.

    Args:
        markdown_path (str or Path): the path to the file.

    Returns:
        List[str]: A list of all level 2 headers in the markdown file.
    """
    level_2_headers = []

    with open(markdown_path) as file:
        for line in file:
            # TODO: Extract level 2 headers here and append
            #   them to `level_2_headers`
            ...

    return level_2_headers

"""
EXERCISE 2, Part 2: Title Case Headers
------------------------

* Implement `title_case_markdown_headers` so that it returns a list of
    all the lines of the markdown file with the level 1, 2 and 3 headers in title case.

For the example from Part 1, `title_case_markdown_headers` should return: 

```markdown
# This Is A Level 1 Header
This is some text.

## This Is A Level 2 Header
* This is a list.

## This Is Another Level 2 Header
<!-- this is a comment -->
```

Notice the headers are in title case. Everything else remains the same.

HINT 1: You can use the `.title()` method on a string to convert it to title case.
HINT 2: Remember to prepend the number signs to the headers ('#', '##', or '###').
HINT 3: You need to append a newline character at the end of the headers ('\n').
"""

def title_case_markdown_headers(markdown_path):
    """Converts all level 1, 2 and 3 headers from a markdown file to title case.

    Args:
        markdown_path (str or Path): the path to the file.

    Returns:
        List[str]: A list of all lines in the markdown file
            with level 1, 2, and 3 headers in title-case.
    """
    markdown_lines = []

    with open(markdown_path) as file:
        for line in file:
            # TODO: Extract all lines to `markdown_lines` with level 1, 2 and 3
            #   headers in title case.
            ...

    return markdown_lines


if __name__ == '__main__':
    l2_headers = extract_level_2_headers(MARKDOWN_PATH)

    print('=' * 50)
    print('\nLevel 2 headers: ', l2_headers)

    assert l2_headers == EXPECTED_LEVEL_2_HEADERS, (
        'extract_level_2_headers returns wrong headers.'
    )

    print()
    print('=' * 50, '\n')

    title_case_markdown = title_case_markdown_headers(MARKDOWN_PATH)

    assert title_case_markdown == EXPECTED_TITLECASE_MARKDOWN, (
        'title_case_markdown_headers does not return correct markdown. '
        'You can print its output and check against data/README_title.md.'
    )

    print('title_case_markdown_headers works as expected!\n')
