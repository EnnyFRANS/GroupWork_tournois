import random

# Create a player's class
class Player:

    def __init__(self, level, health):
        self.level = level
        self.health = health

    def level_up(self):
        self.level += 1

    def loose_health(self):
        self.health -= 1

participant = Player(1, 10)

# Create an enemy's class
class Enemy:

    # Create the enemy's settings
    def __init__(self,creature_name, skill_01, skill_02, creature_level):
        self.creature_name = creature_name
        self.skill_01 = skill_01
        self.skill_02 = skill_02
        self.creature_level = creature_level

    # Make the enemy's level randomly chose base of the player's level
    def level_random(self, player_level):
        return random.randint(player_level -1, player_level +1)

# Creation of 3 objects
creature_01 = Enemy("Pikachu", "thunder", "kiss",0)
creature_02 = Enemy("Wyverne", "Storm", "Rest",0)
creature_03 = Enemy("Troll", "Axe", "Beer",0)

while participant.health > 0:
    player_choice = input("Against which creature would you like to fight ?")




