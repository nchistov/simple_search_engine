import re

from indexer import index

trie = index()

search_string = input('Search something... ').lower()
search_string = re.sub(r'["\',.!?;:/*\-+]', '', search_string)

separators = trie.separators[search_string[0]]


def search_text(text, node):
    current_symbol = text[0]
    urls = []

    if current_symbol not in node.children.keys():
        return []
    else:
        if len(text) > 1:
            urls.extend(search_text(text[1:], node.children[current_symbol]))
        else:
            urls.extend(node.urls)

    return urls


result = []

for sep in separators:
    result.extend(search_text(search_string, sep))

print()

if not result:
    print('Sorry, nothing found.')
else:
    print('Search results:')

    for r in result:
        print()
        print(r)
