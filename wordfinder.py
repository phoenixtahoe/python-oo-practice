"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    def __init__(self, path):
        f = open(path)
        self.words = self.parse(f)
    def parse(self, f):
        return [words.strip() for words in f]
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, f):
        return [words.strip() for words in f if words.strip() and not words.startswith("#")]