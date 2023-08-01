import csv
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent.parent / 'data'


with open(DATA_PATH / 'english_web_word_frequencies.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip header line
    words, word_frequencies = zip(*reader)
    words = tuple(word.strip().lower() for word in words)
    word_frequencies = tuple(int(freq) for freq in word_frequencies)
