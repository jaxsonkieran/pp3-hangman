# Welcome to hangman. All code plus resources used in this project will be credited in the README file.

import random
from words import words
from time import sleep

# Add colors to the program, with help form geeksforgeeks.com for import


class colors:


    '''
    Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold
    '''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'


# Function that get's player name
def ask_player_name():
    """
    Asks player to enter their name. 
    """
    global name
    while True:
        name = input("\n Enter your player name: ")
        if name.isalpha():
            break
        print(colors.fg.red + "Please insert only valid letters (A-Z)." + colors.reset)
    sleep(1)
    print("\nGoodluck, " + colors.fg.cyan + f"{name.capitalize()}" + colors.reset + "!")


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
def check_guess_word(word, guessed_word):
    if guessed_word == word:
        return True
    else:
        return False


# Function to get difficulty from the user input
def get_difficulty():
    """
    Prompt the user to enter the difficulty level.
    Validate the input and return difficulty level.
    """
    while True:
        difficulty = input("Enter your choice (e/m/h): ").strip().lower()
        if difficulty in ['e', 'm', 'h']:
            return difficulty
        else:
            print("Invalid input. Please enter 'e' for Easy, 'm' for Medium, or 'h' for Hard.")

# Function to play the hangman game
def hangman():

    hangman_logo()
    user_welcome()
    ask_player_name()


    # Difficulty selection
    print("Choose your difficulty!\n")
    print(colors.fg.green + "- Enter e for Easy, this will give you 8 lives" + colors.reset)
    print(colors.fg.orange + "- Enter m for Medium, this will give you 6 lives" + colors.reset)
    print(colors.fg.red + "- Enter h for Hard, this will give you 4 lives" + colors.reset)

    difficulty = get_difficulty()
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
        guess = input("Guess a letter: ").lower()
        
        # Validate the user's input
        if len(guess) != 1 or not guess.isalpha():
            print(colors.fg.red + "Please enter a single alphabetical character." + colors.reset)
            continue

        # Check if the guessed letter has already been guessed
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed this letter.")
            continue

        # Check if the guessed letter is in the word
        if guess in word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print(display_hangman(lives))
                print(display_word(word, guessed_letters, incorrect_guesses)) 
                print(colors.fg.green + f"Congratulations {name.capitalize()}!. You've guessed the word correctly!" + colors.reset)
                game_over = True

        else:
            # If the guessed letter is not in the word, add it to incorrect guesses
            incorrect_guesses.append(guess)
            lives -= 1
            print(colors.fg.yellow + f"You have {lives} lives remaining." + colors.reset)
            # Check if the player has run out of lives
            if lives == 0:
                print(colors.fg.red + "You're out of lives, " + f"{name.capitalize()}" + "!" + colors.reset)
                print("The word was, ", word)
                game_over = True

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Yes/No): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing hangman, hope you enjoyed :)")   


# Hangman logo
"""
The word 'hangman' is printed to the terminal, like a logo
in colors before the game begins.
"""
def hangman_logo():
    print(colors.fg.purple + r""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
""" + colors.reset)

# Welcome output for user
def user_welcome():
    """
    WElcome user to the game
    give rules of the game
    choose a level
    """
    print("Welcome to Hangman! \n")
    sleep(1)
    print("Try to guess the random word before you get hung\n")
    sleep(1)
    print("Follow the instructions below to choose a level: Easy, Medium, Hard.\n")
    sleep(1)
    print("----------------------------------------")
    sleep(1)


# Start the game
hangman()