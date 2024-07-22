import unittest
import guessing_game

class TestGame(unittest.TestCase):
    def test_guess_checker_right_answer(self):
        answer = 5
        guess = 5
        result = guessing_game.guess_checker(guess, answer)
        self.assertTrue(result)
        
    def test_guess_checker_wrong_answer(self):
        answer = 5
        guess = 10
        result = guessing_game.guess_checker(guess, answer)
        self.assertFalse(result)
    
if __name__ == '__main__':
    unittest.main()
