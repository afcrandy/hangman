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

def main():
    """
    Run game loop
    """

    # prompt user to begin game or exit program
    while True:
        start_action = input("Press 'p' to play or 'x' to exit\n").lower()
        # handle valid and invalid choices
        if start_action == 'p':
            print()
            break
        elif start_action == 'x':
            return
        else:
            print('Sorry but command was invalid')
            print()
    
    # if user initiates Game, init an instance of Game
    game = Game()

    # print number of letters to user and initial game layout
    print(f"Word selected. It has {game.word_length()} letters")
    print()
    print(game.game_string())
    print()


print_welcome()
main()
