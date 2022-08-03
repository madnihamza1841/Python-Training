"""
The file contains the WordRecord class.
The class can be used to store a single word, with its length, definition and 
pronunciation.
"""

class WordRecord:
    """
    The WordRecord class stores available information about the word.

    Attributes:
        spelling (str): The spelling of the word.
        definition (str): The definition of the word.
        pronunciation (str): The pronunciation of the word.

    Methods:
        None
    """
    def __init__(self, spelling, definition, pronunciation):
        """ 
        Initializes the class object and stores the spelling, definition, 
        pronunciation of the word.

        Arguments:
            spelling (str): The spelling of the word.
            definition (str): The definition of the word.
            pronunciation (str): The pronunciation of the word.
        """
        self.spelling = spelling
        self.definition = definition
        self.pronunciation = pronunciation
