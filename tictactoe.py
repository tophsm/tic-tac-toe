#Tic Tac Toe Game
import math
import random

class Player:
    def __init__(self, letter):
        # letter is either 'X' or 'O'
        self.letter = letter

    def get_move(self, game):
        pass


class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #return super().get_move(game)
        pass

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #return super().get_move(game)
        pass 
    