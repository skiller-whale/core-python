import csv
from pathlib import Path


whale_data = {
    'beluga': 100,
    'orca': 50,
    'narwhal': 25,
    'humpback': 13,
    'fin': 19,
    'bowhead': 57,
    'blue': 98,
    'minkle': 231,
    'sei': 1,
    'gray': 11
}


DATA_PATH = Path(__file__).parent.parent.parent / 'data'
PROFILE_DATA_PATH = DATA_PATH / 'profile_data.csv'


with open(PROFILE_DATA_PATH) as f:
    reader = csv.DictReader(f)
    all_profiles_raw = [dict(x) for x in reader]


def flat_profile(raw_profile):
    """
    Convert a raw profile dictionary to a flattened profile dictionary.

    Args:
        raw_profile (dict): The raw profile dictionary.

    Returns:
        dict: The flattened profile dictionary with 'favourite_shop' as a key
              and 'shop_1', 'shop_2' keys removed.
    """
    d = raw_profile.copy()
    d['favourite_shop'] = raw_profile['shop_1']
    del d['shop_1'], d['shop_2']
    return d


all_profiles = [flat_profile(p) for p in all_profiles_raw]
