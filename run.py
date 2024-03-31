# Welcome to hangman. All code plus resources used in this project will be credited in the README file. 

import random
from words import words

# Function to choose a random word from the words.py list
# This function was really helped by the json file from Kylie Ying in her YT tutorial
def choose_word(words):
    """
    Choose a random word from the 'words.py' file
    skip the invalid words (hyphen or space)
    return the word
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

# Function to display the hangman
def display_hangman(lives):
    stages = [  
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    if lives < len(stages):
        return stages[lives]
    else:
        return stages[-1]  # Return the last stage if lives exceed the length of stages

# Function to check if the guessed letter is in the word

# Function to display the word with blanks and guessed letters
def display_word(word, guessed_letters, incorrect_guesses):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_ "
    
    displayed_word += "\nIncorrect guesses: " + ", ".join(incorrect_guesses)
    return displayed_word

# Function to check if the guessed word matches the chosen word


# Function to play the hangman game
def hangman():
    # Ask the user to enter their name
    name = input("Enter your name: ")
    print(f"Welcome {name}! Let's get ready to play hangman :)")

    # Difficulty selection
    print("Choose your difficulty!")
    print("Enter e for Easy, this will give you 8 lives")
    print("Enter m for Medium, this will give you 6 lives")
    print("Enter h for Hard, this will give you 4 lives")

    difficulty = input("Enter your choice (e/m/h): ").lower()
    if difficulty == "e":
        lives = 8
    elif difficulty == "m":
        lives = 6
    elif difficulty == "h":
        lives = 4
    else:
        print("Invalid input. Defaulting to easy")
        lives = 8
    
    # Choose a random word
    word = choose_word(words)

    # Initialise lists to store guessed letters and incorrect guesses
    guessed_letters = []
    incorrect_guesses = []

    # Initialise game state variables
    game_over = False

    # Main game loop
    while not game_over:
        # Display the current hangman state and the word with guessed letters
        print(display_hangman(lives))
        print(display_word(word, guessed_letters, incorrect_guesses))

        # Prompt the user to guess a letter
        guess = input("Guess a letter: ").upper()
        
        # Validate the user's input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        # Check if the guessed letter has already been guessed
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed this letter.")
            continue

        # Check if the guessed letter is in the word
        if guess in word:
            guessed_letters.append(guess)
            if ''.join(guessed_letters) == word:
                print(display_hangman(lives))
                print(display_word(word, guessed_letters, incorrect_guesses)) 
                print("Congratulations. You've guessed the word correctly!")
                game_over = True

        else:
            # If the guessed letter is not in the word, add it to incorrect guesses
            incorrect_guesses.append(guess)
            lives -= 1
            print(f"You have {lives} lives remaining.")
            # Check if the player has run out of lives
            if lives == 0:
                print("You're out of lives! The word was: ", word)
                game_over = True

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Yes/No): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing hangman, hope you enjoyed :)")   

# Start the game
hangman()