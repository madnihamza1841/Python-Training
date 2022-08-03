
"""
This file is the main file for the typing tester feature. 
"""

import time

from word_record import WordRecord
from helpers import display_helper, typing_tester, track_user_input
from api import RandomWords


def main():
    """
    The function is the main function for the typing tester feature.
    
    The main function creates a RandomWordAPI class for retreiving from API, creates the
    Word object from the data and then passes it on to the typing tester feature.
    
    Arguments:
        None

    Returns:
        None 
    """
    random_word_data = RandomWords().fetch_random_words()
    
    if not isinstance(random_word_data, str):
        word = WordRecord(
            random_word_data["word"], 
            random_word_data["definition"], 
            random_word_data["pronunciation"]
        )
        display_helper("word", word.spelling)
        start_time = time.time()
        user_typing_data = track_user_input()
        user_typing_data["start_time"] = start_time

        typing_tester(user_typing_data, word)   
    else:
        print(random_word_data)

if __name__ == "__main__":
    main()