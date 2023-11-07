import re

from trie import PrefixTree


def index():
    trie = PrefixTree()

    for file in ('first.txt', 'second.txt', 'third.txt'):
        with (open(f'data/{file}') as f):
            text = re.sub(r'["\',.!?;:/*\-+]', '', f.read())

            trie.insert_text(text.lower(), [file])

    return trie
