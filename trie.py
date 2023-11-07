"""
Thanks: https://www.aleksandrhovhannisyan.com/blog/trie-data-structure-implementation-in-python/
"""

from collections import defaultdict


class TrieNode:
    def __init__(self, text='', urls=None):
        self.text = text
        self.children = {}
        self.is_word = False

        if urls is not None:
            self.urls = set(urls)
        else:
            self.urls = set()


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

        self.separators = defaultdict(list)

    def insert(self, word, urls):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i + 1]
                current.children[char] = TrieNode(prefix, urls=urls)
            current = current.children[char]
        current.is_word = True

    def insert_text(self, text, urls):
        current = self.root

        self.separators[text[0]].append(self.root)

        splited_text = text.split()

        for n, word in enumerate(splited_text):
            for i, char in enumerate(word):
                if char not in current.children:
                    prefix = word[0:i + 1]
                    current.children[char] = TrieNode(prefix, urls=urls)
                else:
                    current.children[char].urls.update(urls)
                current = current.children[char]
            current.is_word = True
            if n != len(splited_text) - 1:
                if ' ' not in current.children:
                    current.children[' '] = TrieNode(' ', urls=urls)
                self.separators[splited_text[n + 1][0]].append(current.children[' '])

                current = current.children[' ']

    def find(self, word):
        """
        Returns the `TrieNode` representing the given word if it exists
        and None otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]

        if current.is_word:
            return current

    def starts_with(self, prefix):
        """
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        """
        words = []
        current = self.root
        for char in prefix:
            if char not in current.children:
                # Could also just return words since it's empty by default
                return []
            current = current.children[char]

        self._child_words_for(current, words)
        return words

    def _child_words_for(self, node, words):
        """
        Private helper function. Cycles through all children
        of node recursively, adding them to words if they
        constitute whole words (as opposed to merely prefixes).
        """
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self._child_words_for(node.children[letter], words)
