""" Tests for Hangman """
import unittest
from hangman import Hangman


class TestMethods(unittest.TestCase):
    """ Test for Hangman """

    def test_correct(self):
        """
            Test for situation when user wins
        """
        hangman = Hangman("hello")
        self.assertTrue(hangman.handle_letter('l'))
        self.assertFalse(hangman.handle_letter('a'))
        self.assertTrue(hangman.handle_letter('o'))
        self.assertTrue(hangman.handle_letter('h'))
        self.assertTrue(hangman.handle_letter('e'))
        self.assertTrue(hangman.check_win())
        self.assertEqual(hangman.get_num_mistakes(), 1)
        self.assertEqual(hangman.get_current_word(), "hello")

    def test_incorrect(self):
        """
            Test for situation when user loses
        """
        hangman = Hangman("hello")
        self.assertFalse(hangman.handle_letter('a'))
        self.assertFalse(hangman.handle_letter('a'))
        self.assertFalse(hangman.handle_letter('a'))
        self.assertFalse(hangman.handle_letter('a'))
        self.assertFalse(hangman.handle_letter('a'))
        self.assertTrue(hangman.check_lose())


if __name__ == "__main__":
    unittest.main()
