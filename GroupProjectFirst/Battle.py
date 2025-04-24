from Player import *
from Enemy import *
import random

class Battle:

    def __init__(self, game):
        self.game = game
        self.player = game.player


    def select_creature(self):
        creature_selected = False
        while not creature_selected:
            print("Please select an enemy")
            user_input  = input("Input 0, 1 or 2")
            try:
                user_choice = int(user_input)
            except:
                print("Your input is not correct. Try again")
                continue

            if user_choice in range(len(self.game.creatures)):
                self.creature = self.game.creatures[int(user_choice)]
                self.creature.level = self.creature.level_random(self.player.level)
                creature_selected = True
                print("You selected {}".format(self.creature.name))
            else:
                print("Your input is not correct. Try again")

    #def define_level_of_creature(self):         # maybe better in class Creature?

    def battle_process(self):
        input("Press any key to start the battle")
        if self.player.level > self.creature.level:
            print("Congratulations! You won!")
            self.player.level_up()
        else:
            print("You lost")
            self.player.loose_health()
        print("Your level is now {}, your health is {}".format(self.player.level, self.player.health))






