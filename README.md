# Hangman 
Welcome to my interactive Hangman game built using python. 

# Table of Contents
* [Project Overview](#project-overview)
* [Game Flowchart](#game-flowchart)
* [How To Play](#how-to-play)
* [Features](#features)
* [Testing](#testing)
* [CI Python Linter](#pep8-validator-code-institute)
* [Bugs](#bugs)
* [Improvements](#improvement)
* [Deployment](#deployment-to-heroku)
* [Credits](#credits)

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
Some colors were included for aesthetic puposes and as a way to guide the player, like the easy level is green, medium is orange, and hard is red. Also, when the user enters their name (cyan), when they lose (red), and when they win (green).

* Welcome / beginning, the player is greeted with the below and instructions. 
<img src="assets/welcome_hg.JPG">

* The player then chooses their difficulty and the number of lives is reflected.
<img src="assets/player_name_choice.JPG">

* A random word is generated for the player to guess from our list. The word is shown blank with underlines symbolising the letter. 
<img src="assets/guess_letter.JPG">

* When the players makes a guess that is incorrect, it is added to the incorrect guesses list and a life is lost, the hangman starts to build.
<img src="assets/incorrect_g.JPG">

* When the player gets a guess right, it is added to the space where the letter is.
<img src="assets/correct_g.JPG">

* When the player loses, and it is over, they are told the word, it is also colored in red.
<img src="assets/incorrect_guess.JPG">

* When the player wins, they are congratulated and it is in green. (The word was removed on final edit as this didn't make sense since they would know the word if they won!)
<img src="assets/correct_guess.JPG">

* After, the player is always asked if they want to play again.

* For users already guessing a letter, it looks like this,
<img src="assets/already_guessed.JPG">

* Invalid input is also handled like so,
<img src="assets/invalid_input.JPG">



# Testing
* Tested for various bugs and functionality but inputting incorrect data, etc.
* Tested for scenarios with successful guesses (valid letters only)
* This game was tested using Firefox, Google Chrome and Internet Explorer.

# PEP8 Validator [Code Institute](https://pep8ci.herokuapp.com/#)
* I used Code Institutes Python Linter. Which can be found [here](https://pep8ci.herokuapp.com/#) to validate my python code.
* All errors and warnings were fixed, bar the warrings for my Hangman logo and the hangman drawing itself (clearing whitespace). This would of affected the look and functionality of the game so I chose to ignore these errors. 
<img src="assets/pep8_ci.JPG">
* Other errors such as not leaving to blank lines between the comment and the function, or indentations, or some issues with lines over 79 characters long were fixed.

# Bugs
1. The first bug was when the hangman game would not display the word in my choose_word function. However, it was down to my misspelling of skip and in the while loop.
2. When entering yes to play again, it wasn't letting me. I fixed this by adding a .lower() method instead of .upper() and it seemed to work correctly after that.
3. If the user guessed a letter, that was correct it was not adding it to the blank spaces provided. With the help of [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w) and [Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8) I was able to fix this issue!
4. Another problem I found, when I wanted to add some color to my program to make it look better, I really struggled. If I added a color to the user name, it would color everything after that, etc! But the code on [GeeksForGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/) helped me solve this issue. 
5. Finally, when using the CI python linter to validate my code, I may have copied in my hangman function incorrectly and it threw my while loop indentation out of whack. This threw me a lot as the game would suddenly end after 1, or 2 or 3 guesses if I still had lives left. But thankfully I could see the indentation problem after some help from a friend. 


# Improvement
* Level of difficulty could be word length based. 
* You could have a level where there is some help involved, e.g. a certain letter is inserted at the beginning to help you.
* Similarly to the above, code could be written to give a user on their last life a helpline, do they want a hint?

# Deployment to Heroku
This project was deployed on Heroku in the following way:

1. Fork or clone this repository.
2. Create a new Heroku app using a different name.
3. Go to 'Deploy' Tab.
<img src="assets/deploy_tab.JPG">
4. Choose Connect to GitHub account.
5. Search for the repo you want to deploy. The name must match the name on github.
<img src="assets/connect_github.JPG">
6. Click 'Connect'.
7. Select automatic or manual deployment.
8. Choose which branch.
<img src="assets/deploy_branch.JPG">
9. Click deploy.
10. When deployment is finished, go to settings to configure vars and buildpacks.
11. 'Reveal config vars, we need to add PORT as the key, and 8000 as the value.
<img src="assets/config_Vars.JPG">
12. Add buildpacks python and node.js, ensure they are in that order.
<img src="assets/buildpacks.JPG">
13. Ensure you now redploy before opening! 

# Credits
There were two main tutorials that really really helped me with this project, that was [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w) and [Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8)

Before coming to Code Institute, I actually started with Harvards free CS50 Intro to Python course so the code came back to me while writing this project.

* [GeeksForGeeks](https://www.geeksforgeeks.org/) Used for some methods and fact checking. It was also how I fixed my color bug.

* Code Institute Slack Channel and Members were also super helpful in getting me to here!

* StackOverflow
* [Lucid - FlowChart](https://www.lucidchart.com/pages/landing/process-map-software?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_phrase_&km_CPC_CampaignId=1490375424&km_CPC_AdGroupID=55688905897&km_CPC_Keyword=%2Blucid%20chart%20%2Bprocess%20%2Bmap&km_CPC_MatchType=b&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433234840&km_CPC_TargetID=kwd-467205741059&km_CPC_Country=1007848&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=Cj0KCQjw2a6wBhCVARIsABPeH1sAjmN0qH0EwuViqQ_ssmL6wAxvjYoCcutnEAWXHUxr-ho-rO1cc9EaAq2DEALw_wcB)

