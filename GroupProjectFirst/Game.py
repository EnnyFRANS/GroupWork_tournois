from Player import *
from Enemy import *
from Battle import *
import random

class Game:
    num_of_creatures = 3

    def __init__(self):
        self.creatures = [Enemy("Pikachu"), Enemy("Wyverne"), Enemy("Troll")]
        self.player = Player(1,10)
        print("Welcome to the tourney, " + self.player.name)


game = Game()
is_game_over = False
while not is_game_over:
    battle = Battle(game)
    battle.select_creature()
    battle.battle_process()
    if game.player.health <= 0:
        is_game_over = True
        print("Game over. You have reached level {}".format(game.player.level))





