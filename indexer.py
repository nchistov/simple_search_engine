import re
import os

from trie import PrefixTree


def index():
    trie = PrefixTree()

    for file in os.listdir('data/'):
        with (open(f'data/{file}') as f):
            text = re.sub(r'["\',.!?;:/*\-+]', '', f.read())

            trie.insert_text(text.lower(), [file])

    return trie
