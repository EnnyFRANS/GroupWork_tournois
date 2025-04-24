import random

# Create an enemy's class
class Enemy:

    # Create the enemy's settings
    def __init__(self,creature_name, skill_01, skill_02):
        self.creature_name = creature_name
        self.skill_01 = skill_01
        self.skill_02 = skill_02
        self.enemy_level = 0

    # Make the enemy's level randomly chose base of the player's level
    def level_random(self, player_level):
        return random.randint(player_level -1, player_level +1)

# Creation of 3 objects
creature_01 = Enemy("Pikachu", "thunder", "kiss")
creature_02 = Enemy("Wyverne", "Storm", "Rest")
creature_03 = Enemy("Troll", "Axe", "Beer")