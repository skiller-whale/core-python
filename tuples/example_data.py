import csv
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / 'data'
PROFILE_DATA_PATH = DATA_PATH / 'profile_data.csv'


with open(PROFILE_DATA_PATH) as f:
    reader = csv.DictReader(f)
    all_profiles_raw = [dict(x) for x in reader]


def flat_profile(raw_profile):
    d = raw_profile.copy()
    d['favourite_shop'] = raw_profile['shop_1']
    del d['shop_1'], d['shop_2']
    return d


all_profiles = [flat_profile(p) for p in all_profiles_raw]
