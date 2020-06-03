"""
Special Word Finder: finds random words from a dictionary.
- leaves out spaces and comments
"""

from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """
    A class used to compile words from a given text file
    without spaces or comments

    Attributes
    ----------
    words: lst
        list of words from file without spaces or comments
    ----------    

    >>> wf = SpecialWordFinder("special_words.txt")
    9 words read

    >>> wf.words
    ['kale', 'parsnips', 'apple', 'mango']
    """

    def __init__(self, file_path):

        super().__init__(file_path)

        self.words = [
            word for word in self.words if word != "" and not word.startswith("#")
        ]
