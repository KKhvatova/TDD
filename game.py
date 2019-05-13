from random import randint
import random


class Bowling:

    def __init__(self):
        self.score = 0

    def total_score(self, score):
        total_score = 0
        for my_round in score:
            if len(my_round) == 3:
                if my_round[0] == 10:
                    total_score += self.strike(my_round)
                else:
                    total_score += self.spare(my_round)
            elif len(my_round) == 2:
                total_score += sum(my_round)
            else:
                return 'error in game score'
        return total_score

        return total_score

    def strike(self, pin):
        first_strike = pin[0]
        if first_strike == 10:
            total_score = sum(pin)
            return total_score
        else:
            return 'not a strike'

    def spare(self, pin):
        if (pin[0]+pin[1]) == 10:
            total_score = sum(pin)
            return total_score
        else:
            return 'not a spare'
