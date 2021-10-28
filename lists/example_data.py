import csv
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / 'data'

FEMALE_FILE = DATA_PATH / 'popular_female_names_1990s.csv'
MALE_FILE   = DATA_PATH / 'popular_male_names_1990s.csv'


def _read_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


def _read_name_list(path):
    name_data = _read_csv(path)
    return [item['Name'] for item in name_data]


girls_names = _read_name_list(FEMALE_FILE)
boys_names = _read_name_list(MALE_FILE)
