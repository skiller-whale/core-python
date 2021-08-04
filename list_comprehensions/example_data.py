import json
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / 'data'
WORD_LIST_FILE = DATA_PATH / 'words_list.txt'


with open(WORD_LIST_FILE) as f:
    word_list = sorted(word.strip().lower() for word in f.readlines())
