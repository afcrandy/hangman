class Game:
    """
    Creates an instance of Game
    """

    def __init__(self):
        self.word = "alternative"
        self.difficulty = 'easy'
        self.correct_guesses = set()
        self.incorrect_guesses = set()
    
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
    
    def guesses_left(self):
        """
        Return whether user has any guesses remaining
        """
        # determine number of guesses allowed based on difficulty
        guesses_allowed = 10 if self.difficulty == 'easy' else 7
        return len(self.incorrect_guesses) < guesses_allowed
    
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
        list_of_letters = sorted(self.correct_guesses.union(self.incorrect_guesses))
        return ' '.join(list_of_letters)
