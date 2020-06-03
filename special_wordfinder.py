"""
Special Word Finder: finds random words from a dictionary.
- leaves out spaces and comments
"""

from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):

    def __init__(self, file_path):

        super().__init__(file_path)

        self.words = [
            word for word in self.words if word != "" and not word.startswith("#")
        ]
