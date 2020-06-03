"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:

    def __init__(self, file_path):
        self.words = self.generate_list(file_path)

    def generate_list(self, file_path):
        file = open(file_path, "r")
        words_list = [line.strip("\n") for line in file]
        file.close()
        print(f"{len(words_list)} words read")
        return words_list

    def random(self):
        return choice(self.words)
