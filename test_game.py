from unittest import TestCase
import game


class GameTest(TestCase):

    def test_score(self):
        bowling = game.Bowling()
        bowling.score = 11
        self.assertEqual(bowling.score, 11)

    def test_total_score(self):
        bowling = game.Bowling()
        total_score = bowling.total_score([[10, 5, 4], [5, 5, 6], [3, 4]])
        self.assertEqual(total_score, 42)

    def test_strike(self):
        bowling = game.Bowling()
        strike = bowling.strike([5, 5, 6])
        self.assertEqual(strike, 'not a strike')

    def test_spare(self):
        bowling = game.Bowling()
        spare = bowling.spare([4, 5, 6])
        self.assertEqual(spare, 'not a spare')
