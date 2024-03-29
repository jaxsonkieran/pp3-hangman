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
    letters_guessed = set() # what the user guesses
    # getting user input
    user_guess = input("Guess a letter: ").upper()
    if user_guess in alphabet - letters_guessed:
        letters_guessed.add(user_guess)
        if user_guess in word_letters:
            word_letters.remove(user_guess)

    elif user_guess in letters_guessed:
        print("You've already guessed this letter. Please try again.")
    
    else:
        print("Error. Please type in a valid letter.")

user_input = input("Please type in a letter: ")
print(user_input)
    