import random

# Create an enemy's class
class Enemy:

    # Create the enemy's settings
    def __init__(self, name, power):
        self.name = name
        self.creature_level = 0
        self.power = power

    # Make the enemy's level randomly chose base of the player's level
    def level_random(self, player_level):
        return random.randint(player_level -1, player_level +1)