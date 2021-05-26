import json
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / 'data'
WORD_LIST_FILE = DATA_PATH / 'words_list.txt'
FILMS_FILE = DATA_PATH / 'films_by_genre.json'


with open(WORD_LIST_FILE) as f:
    words = {word.strip().lower() for word in f.readlines()}


with open(FILMS_FILE) as f:
    _films_by_genre_raw = json.load(f)


films_by_genre = {
    category: set(films) for category, films in _films_by_genre_raw.items()
}
