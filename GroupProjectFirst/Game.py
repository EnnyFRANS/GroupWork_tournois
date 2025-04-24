from Personage import *
from Creature import *
from Battle import *
import random

class Game:
    num_of_creatures = 3

    def __init__(self):
        self.creatures = []
        self.creatures.append(Creature("Pikachu"))
        self.creatures.append(Creature("Wyverne"))
        self.creatures.append(Creature("Troll"))
        self.personage = Personage()
        print("Welcome to the tourney, " + self.personage.name)



game = Game()
is_game_over = False
while not is_game_over:
    battle = Battle(game)
    battle.select_creature()
    battle.battle_process()
    if game.personage.health <= 0:
        is_game_over = True





