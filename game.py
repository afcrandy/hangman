class Game:
    """
    Creates an instance of GameRound
    """

    def __init__(self):
        self.word = "alternative"
        self.difficulty = 'easy'
        self.correct_guesses = []
        self.incorrect_guesses = []
    
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
