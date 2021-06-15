from collections import defaultdict
from csv import DictReader
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / 'data'
FEMALE_FILE = DATA_PATH / 'popular_female_names_by_decade.csv'
MALE_FILE = DATA_PATH / 'popular_male_names_by_decade.csv'


def get_name_popularity_by_year(path):
    names = defaultdict(dict)

    with open(path) as data_file:
        reader = DictReader(data_file)

        for item in reader:
            year = int(item['Year'])
            name = item['Name'].lower()
            names[year][name] = int(item['Count'])
    return dict(names)


girls_popularity_by_decade = get_name_popularity_by_year(FEMALE_FILE)
boys_popularity_by_decade = get_name_popularity_by_year(MALE_FILE)
