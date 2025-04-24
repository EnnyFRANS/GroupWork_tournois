from Personage import *
from Creature import *
import random

class Battle:

    def __init__(self, game):
        self.game = game
        self.personage = game.personage


    def select_creature(self):
        creature_selected = False
        while not creature_selected:
            user_choice  = input("Please select an enemy")
            if int(user_choice).is_integer() and int(user_choice) in range(len(self.game.creatures)):
                self.creature = self.game.creatures[int(user_choice)]
                creature_selected = True
                print("You selected {}".format(self.creature.name))
            else:
                print("Your input is not correct. Try again")

    #def define_level_of_creature(self):         # maybe better in class Creature?

    def battle_process(self):
        input("Press any key to start the battle")
        if self.personage.level > self.creature.level:
            print("Congratulations! You won!")
            self.personage.level += 1
        else:
            print("You lost")
            self.personage.health -= 1
        print("Your level is now {}, your health is {}".format(self.personage.level, self.personage.health))






