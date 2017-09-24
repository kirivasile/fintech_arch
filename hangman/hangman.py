""" Implementation of game Hangman """

class Hangman(object):
    """ Class of game itself"""

    def __init__(self, word):
        """
            Initialize the game
            word : Initial word for game
        """
        self._word = word
        self._num_mistakes = 0
        self._tokens = list(word)
        self._current_word = ["*"] * len(self._tokens)

    def handle_letter(self, letter):
        """
            Handle the incoming letter
            letter : incoming letter
        """
        if letter in self._tokens:
            indices = [i for i in xrange(len(self._tokens)) if self._tokens[i] == letter]
            for idx in indices:
                self._current_word[idx] = self._tokens[idx]
            return True
        else:
            self._num_mistakes += 1
            return False

    def get_num_mistakes(self):
        """
            Get the number of mistakes made by user
        """
        return self._num_mistakes

    def get_current_word(self):
        """
            Get current word the user succeeded to guess
        """
        return "".join(self._current_word)

    def check_win(self):
        """
            Check if user won
        """
        return "*" not in self._current_word

    def check_lose(self):
        """
            Check if user lost
        """
        return self._num_mistakes >= 5


def play_game():
    """
        Game procedure
    """
    hangman = Hangman("hello")
    while True:
        print "Guess a letter:"
        letter = raw_input()
        if len(letter) > 1:
            print "Enter only one letter"
            continue
        if hangman.handle_letter(letter):
            print "Hit!\n"
        else:
            print "Missed, mistake %d out of 5\n" % hangman.get_num_mistakes()
        print "The word: %s\n" % "".join(hangman.get_current_word())
        if hangman.check_win():
            print "You won!"
            return
        if hangman.check_lose():
            print "You lose!"
            return


if __name__ == "__main__":
    play_game()
