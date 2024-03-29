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

def hangman():
    word = choose_word(words)
    word_letters = set(word) # keeping track of whats already been guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user guesses

    user_guess = input("Guess a letter: ").upper()

user_input = input("Please type in a letter: ")
print(user_input)
    