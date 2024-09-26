from art import *
from game import Game

def print_welcome():
    """
    Print the welcome screen at the beginning of the game
    """
    # insert ASCII art 'Hangman' to replace below
    print(WELCOME_LOGO)
    print('by Andrew Reid')
    print()

def is_valid(guess):
    """
    Test if a provided guess is a valid one
    """
    # assert guess is a single character in length
    if len(guess) != 1:
        return False
    
    # assert guess is a letter
    if guess not in 'abcdefghijklmnopqrstuvwxyz':
        return False
    
    # return true otherwise
    return True

def print_game_state(game):
    """
    Takes a Game object and prints out the current state of the board
    Includes the Hangman, game string, and incorrect guess
    """
    # determine difficulty and add offset if playing on 'easy'
    offset = 0 if game.difficulty == 'easy' else 4

    print(game.game_string())
    print()
    print(STAGE_IMAGES[game.wrong_guesses() + offset])
    print()
    print(f"Already guessed: {game.guessed_letters()}\n")

def main():
    """
    Run game functions
    """

    # prompt user to begin game or exit program
    while True:
        prompt = "Press 'p' to play, 'h' for hard difficulty, or 'x' to exit"
        start_action = input(f"{prompt}\n").lower()
        # handle valid and invalid choices
        if start_action == 'p' or start_action == 'h':
            print()
            break
        elif start_action == 'x':
            return
        else:
            print('Sorry but command was invalid')
            print()
    
    # if user initiates Game, init an instance of Game and set difficulty
    game = Game()
    game.difficulty = 'hard' if start_action == 'h' else 'easy'

    # print number of letters to user and initial game layout
    print(f"Word selected. It has {game.word_length()} letters")
    print()
    print_game_state(game)

    # game loop
    while game.guesses_left() and not game.complete():
        guess = input('Guess a letter: ').lower()
        print('\n\n')

        # if guess is valid
        if is_valid(guess):
            if game.already_guessed(guess):
                print("You've already guessed that letter")
                print("Please select another\n")
                continue
            else:
                # handle valid guess
                if game.check(guess):
                    print(f"Well done, {guess} is in the word\n")
                else:
                    print(f"Unlucky, {guess} is not in the word\n")
                
                # print out game state
                print_game_state(game)
        else:
            print('Invalid character. Please select another\n')
            continue


print_welcome()
main()
