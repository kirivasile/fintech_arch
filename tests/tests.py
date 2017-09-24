""" Tests for Hangman """
from hangman import Hangman


def test_correct():
    """
        Test for situation when user wins
    """
    hangman = Hangman("hello")
    assert hangman.handle_letter('l')
    assert not hangman.handle_letter('a')
    assert hangman.handle_letter('o')
    assert hangman.handle_letter('h')
    assert not hangman.handle_letter('e')
    assert hangman.check_win()
    assert hangman.get_num_mistakes() == 1
    assert hangman.get_current_word == "hello"


def test_incorrect():
    """
        Test for situation when user loses
    """
    hangman = Hangman("hello")
    assert not hangman.handle_letter('a')
    assert not hangman.handle_letter('a')
    assert not hangman.handle_letter('a')
    assert not hangman.handle_letter('a')
    assert not hangman.handle_letter('a')
    assert hangman.check_lose()
