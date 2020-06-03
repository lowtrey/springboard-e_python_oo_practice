"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    """
    A class used to compile words from a given text file

    Attributes
    ----------
    words: lst
        list of words from file
    ----------    

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf = WordFinder("special_words.txt")
    9 words read
    """

    def __init__(self, file_path):
        self.words = self.generate_list(file_path)

    def generate_list(self, file_path):
        """Generates a list of words from a given file"""

        file = open(file_path, "r")
        words_list = [line.strip("\n") for line in file]
        file.close()
        print(f"{len(words_list)} words read")
        return words_list

    def random(self):
        """Returns random word from words list"""
        return choice(self.words)
