# Hangman 
Welcome to my interactive Hangman game built using python. 

# Table of Contents

# Project Overview
This project is based on the game Hangman. Playing this game, the user must guess the full word before the hangman is hung (drawn). This is done by guessing each letter in the word. 

If the guess is right, it is placed in the blank spaces that make up the word. If it is not, it is placed in the incorrect guesses section and the user loses a life, the construction of the hanging man starts. The word must be guessed before the user runs out of lives.

The user can play the game at three different levels of difficulty, based on the number of lives. 8 lives for Easy, 6 lives for Medium and 4 lives for Hard.

At the beginning of the game, the player is asked to give their name, which is then held and used to wish them goodluck, and at the end of the game to congratulate them or tell them they've lost. 

Once the game is finished, the player is asked if they'd like to play again. Entering yes will restart the game with a new word and they can choose the difficulty again too. Entering no, will conclude the game. 

# Game Flowchart
When planning the game, it was important to build a full game flow so that I could think about the functions, what commands and what user inputs would be needed for everything to work. To build this, I created a flowchart using Lucid.
<img src="assets/hangman.jpeg">

# How to Play
The player chooses the difficulty level and a random word will be showing use (_) in place of the letters. The player starts to guess letters one at a time (if the player does not enter a valid letter or one at a time there will be a error). If the letter is in the word it will fill the location of the _ blank. If the letter is not in the word, the user loses a life, it will say how many lives remain, and the letter will be added to the incorrect guesses section. The hangman will also start to build.

The player keeps guessing until completing the word. For winning the game, the user will be congratulated. For losing the game, the user will be told and it will tell them what the word was so they know. 

The user can choose to play again or exit.

# Features

# Testing
* Tested for various bugs and functionality but inputting incorrect data, etc.
* Tested for scenarios with successful guesses (valid letters only)
* This game was tested using Firefox, Google Chrome and Internet Explorer.

# PEP8


