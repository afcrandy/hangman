# Hangman

Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can attempt to beat the computer by correctly guessing the letters which make up the randomly selected word. Each incorrect guess contributes one piece to build an image of gallows and a hanging man. If the player guesses the letters in the word correctly before exceeding the allowed number of incorrect guesses (10 guesses in easy mode and 6 in hard) they will win the game.

[Here is the live version of the project](https://hangman-ci-project3-ar-bb3390253c6a.herokuapp.com/)

![Project Appearance Responsive](/assets/images/cli-hangman-amiresponsive.png)

## How to play

Hangman is based on the classic game of the same name. You can read about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

In my version, the player selects a difficulty level (easy or hard) and the computer random selects a word.

The game tells the player how many letters there are in the word, and prints out the word - with '_' characters for as-yet unguessed letters. There is an ASCII image which shows the state of the hangman and the list of letters guessed so far each round. 

Next, the player must guess letters until they've got the whole word before the number of incorrect guesses is exceeded and the Hangman image is complete.

The player has 10 guesses on easy difficulty, and 6 on hard.

## Features

### Existing Features

* Instructions for how to play the game
![Game Instructions](/assets/images/game-instructions.png)

* Random word selection
    * The computer selects a random word from existing word bank
    * The player cannot see the word or list of words in the word bank

* Select a difficulty level
    * The game prompts the player to select either the 'easy' or 'hard' difficulty level
    * The player will be allowed 10 incorrect letter guesses at the easy level and 6 incorrect guesses at the hard level
    ![Difficulty Level Select](/assets/images/difficulty-select.png)

* Accepts user input

* Maintains scores
    * The game keeps track of the letters which have been previously guessed by the player during a round
    * The game represents the number of incorrect guesses with the ASCII hangman image

* Input validation
    * All input is validated to be one alphabet character
    ![Invalid Character Feedback](/assets/images/invalid-character-feedback.png)

* Feeds back user progress round-by-round
    * The hangman image is printed to the terminal and updated with each incorrect guess made by the player
    * If the player wins they receive a message of 'congratulations' and if they lose 'better luck next time'
    ![Round by Round Feedback](/assets/images/round-feedback.png)

* Data maintained in class instances

* Error handling for missing wordlist
    * If word list cannot be found user is notified with an error code

* Capability to initiate new game after finishing one
    * The game prompts the player to decide if they would like to play another round or exit the game
    ![End of Game Options](/assets/images/end-of-game-restart-option.png)

### Future Features

* Allow words to contain non-alphabet characters
* Allow phrases instead of just single words

## Data Model

I have used a Game class to model the state of the game.

The Game class stores the word, the difficulty selected and the letters guessed (both correct and incorrect).

It also has methods to extrapolate further information about the state of the game from these properties; such as how many incorrect guesses the player has left, has the game ended either in victory or defeat, is an input character valid, already guessed or correct.

## Testing

I have manually tested this project by doing the following:
* Passed the code through a PEP8 linter and confirmed there are no problems
* Given invalid inputs: numbers, multiple characters, repeat inputs and no input
* Tested in my local terminal, in my development terminal in GitPod and in the deployed terminal

### Bugs

#### Solved Bugs

* During development I found the same word kept getting selected for the game. I had forgotten that `readlines()` returned strings with a newline character at the end - all except the final word in the file. My filter when removing invalid words that might be in the wordlist excluded all words containing any non-alphabet characters, including whitespace. I fixed this by removing the newline character before filtering the words.

* After this fix I was getting extraneous '_' characters at the end of the string that shows the player's progress towards guessing all the letters. This was because the newline was being removed for the filter, but not from the actual word when stored in the Game instance. I used `strip()` when initialising the instance to remove all whitespace.

* I was getting a SyntaxError when I first added my ASCII art Hangman. It turned out this is because the images inlude the '\\' character, which is used in escape sequences, but the characters following it did not constitute valid sequences. So I had to escape the backslashes with another backslash.

#### Remaining Bugs

* No bugs remaining

### Validator Testing

* PEP8 (using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/))
    - No errors were found for [run.py](run.py) or [game.py](game.py)
    - [art.py](art.py) returned 10 `E128` errors and 1 `E124` error - these were due to using multiline strings to store the Hangman ASCII art but if I indented them as the linter wanted me to I found the images sometimes behaved incorrectly

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku

Steps for deployment:
* Fork or clone this repository
* Create a new heroku app within your Heroku account
* Add Python and NodeJs buildpacks, in that order in app Settings tab
* Also in the Settings tab, add a Config Var with key `PORT` amd value `8000`
* In the Deploy tab, link the Heroku app to the repository
* Click **Deploy**

Constraints:
* The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line
* If using the `input` method, prompts provided must end with the newline character `\n`

## Credits

* Code Institute for the deployment terminal
* [This ASCII Text Generator](https://ascii.co.uk/text) for the logo for the game
* The apparently defunct http://www.mieliestronk.com/wordlist.html via [this repo from Tom25](https://github.com/Tom25/Hangman/tree/master) for the wordlist
* [W3S reference for RegEx](https://www.w3schools.com/python/python_regex.asp) for help filtering invalid words and characters
* Code Institute diploma in Full Stack Development (specifically the section on [Python I/O & Exception Handling](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/e38bbf480aec434f9f00f0bf6285e35c/60c772e2068242b88b56998cd2023621/)) for the file loading exception-handling code
