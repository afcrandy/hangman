import random
from art import STAGE_IMAGES


class Game:
    """
    Creates an instance of Game
    """

    # define game instructions for all games
    instructions = """
    Guess letters you think are in the word to save the man
    Each wrong guess gets the man closer to his doom
    Hard mode begins with the gallows already set up
    """

    def __init__(self, wordlist):
        self.difficulty = 'easy'
        self.correct_guesses = set()
        self.incorrect_guesses = set()

        # select random word from list passed in to init
        self.word = random.choice(wordlist).lower().strip()

    def __str__(self):
        """
        How to render Game object when printed
        Prints out current state of game board
        Includes the Hangman, game string and incorrect guesses
        """
        # determine difficulty and add offset if playing on 'easy'
        offset = 0 if self.difficulty == 'easy' else 4
        return STAGE_IMAGES[self.wrong_guesses() + offset]

    def word_length(self):
        return len(self.word)

    def game_string(self):
        """
        Print the guessed progress so far with correct letters
        """
        progress = []
        for char in self.word:
            progress.append(char if char in self.correct_guesses else '_')
        return ' '.join(progress)

    def wrong_guesses(self):
        """
        Return how many guesses user has remaining
        """
        return len(self.incorrect_guesses)

    def guesses_left(self):
        """
        Return whether user has any guesses remaining
        """
        # determine number of guesses allowed based on difficulty
        guesses_allowed = 10 if self.difficulty == 'easy' else 6
        return self.wrong_guesses() < guesses_allowed

    def complete(self):
        """
        Return whether game_string contains any '_' indicating not finished
        """
        return '_' not in self.game_string()

    def check(self, guess):
        """
        Given a valid as-yet unguessed character, check if in word
        Add guess to correct set and return whether success or not
        """
        guess_was_correct = guess in self.word

        if guess_was_correct:
            self.correct_guesses.add(guess)
        else:
            self.incorrect_guesses.add(guess)

        return guess_was_correct

    def already_guessed(self, guess):
        """
        Return whether a given valid character has already been guessed
        """
        return guess in self.correct_guesses.union(self.incorrect_guesses)

    def guessed_letters(self):
        """
        Returns an ordered list of all the letters guessed so far
        """
        all_guesses = self.correct_guesses.union(self.incorrect_guesses)
        list_of_letters = sorted(all_guesses)
        return ' '.join(list_of_letters)
