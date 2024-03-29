# Welcome to hangman. All code plus resources used in this project will be credited in the README file. 

import random
from words import words

def choose_word(words):
    """
    Choose a random word from the 'words.py' file
    skid the invalid words (hypen or space)
    return the word
    """
    word = random.choice(words)
    while '-' or ' ' in word:
        word = random.choice(words)
    return word