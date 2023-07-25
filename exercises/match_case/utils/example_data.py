import csv
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / 'data'
MARKDOWN_PATH = DATA_PATH / 'README.md'


EXPECTED_LEVEL_2_HEADERS = [
    'how to submit a good query',
    'example queries',
    'limitations'
]

with open(DATA_PATH / 'README_title.md') as file:
    EXPECTED_TITLECASE_MARKDOWN = file.readlines()
