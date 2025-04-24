from Personage import *
from Creature import *
from Battle import *
import random

class Game:
    num_of_creatures = 3

    def __init__(self):
        self.creatures = []
        for i in range(self.num_of_creatures):
            self.creatures.append(Creature("blabla"))
        self.personage = Personage()
        print("Welcome to the tourney, " + self.personage.name)

    def is_game_over(self):
        if self.personage.health == 0:
            return True
        else:
            return False


game = Game()
is_game_over = False
while not is_game_over:
    battle = Battle(game)
    battle.select_creature()
    battle.battle_process()
    if game.is_game_over:
        is_game_over = True




