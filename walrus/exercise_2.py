import os
from pathlib import Path
from zlib import compress, decompress
import filecmp


DATA_PATH = Path(__file__).parent.parent / 'data'
OUTPUT_PATH = Path(__file__).parent / 'data'

FILE_NAME = 'profile_data'
INPUT_FILE = DATA_PATH / 'profile_data.csv'
DECOMPRESSED_FILE = OUTPUT_PATH / 'profile_data.csv'


# pylint: disable=pointless-string-statement
"""
EXERCISE 2: READING FILES IN CHUNKS
------------------------

The code below reads and compresses the profile data CSV file in chunks.
The function `compress_data` is responsible for splitting the file into
    chunks and calling `compress_chunk` on each chunk.

The function `decompress_data` does the opposite.

    * Use `:=` to simplify `compress_data`. For this part you do not
        need to edit any other functions.
        * The `assert` statement at the end checks that a call
            to `compress_data`/`decompress_data` gives back the original file.
    * Once done, think about whether using `:=` improved this code.
        * What are the pros/cons of using `:=` here?

[EXTENSION]
    * Use `:=` to further simplify `decompress_data`.
        * Did using `:=` improve `decompress_data`?
"""


def get_chunk_filename(path, name, chunk_id):
    """Returns a chunk filename."""
    return path / f'{name}_{chunk_id}.dat'


def compress_chunk(chunk, chunk_id, output_path, output_name):
    """Compresses a chunk of data and writes it to a file."""
    compressed = compress(chunk)
    out_path = get_chunk_filename(
        output_path, output_name,
        chunk_id
    )

    with open(out_path, 'wb') as output_file:
        output_file.write(compressed)


# YOUR CODE GOES HERE
def compress_data(input_path, output_path, output_name, chunk_size=20480):
    """Compresses a file in chunks and write to file(s).

    Args:
        input_path (Path): The input file path.
        output_path (Path): The output directory.
        output_name (str): The output file name.
        chunk_size (int, optional): Chunk size. Defaults to 20480.

    The function will write files for each chunk:
        <output_path>/<output_name>_0.dat
        <output_path>/<output_name>_1.dat
        ...
    """
    # * Use `:=` to simplify `compress_data`. For this part you do not
    #    need to edit any other functions.
    with open(input_path, 'rb') as input_file:
        chunk_id = 0

        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break

            compress_chunk(chunk, chunk_id, output_path, output_name)
            chunk_id += 1


def decompress_data(input_path, input_name, output_path):
    """Decompresses data and writes to file."""
    chunk_id = -1
    with open(output_path, 'wb') as output_file:
        while True:
            in_path = get_chunk_filename(
                input_path, input_name,
                chunk_id := chunk_id + 1
            )

            try:
                with open(in_path, 'rb') as input_file:
                    output_file.write(
                        decompress(input_file.read())
                    )
            except FileNotFoundError:
                break


if __name__ == '__main__':
    # Empty output data directory
    for path in OUTPUT_PATH.iterdir():
        if not path.stem.startswith('.'):
            os.remove(path)

    compress_data(INPUT_FILE, OUTPUT_PATH, FILE_NAME)
    decompress_data(OUTPUT_PATH, FILE_NAME, DECOMPRESSED_FILE)

    assert filecmp.cmp(INPUT_FILE, DECOMPRESSED_FILE), (
        'Compressed/decompressed file does not match original!'
    )

    print(f'Successfully compressed and decompressed {INPUT_FILE.stem}')
