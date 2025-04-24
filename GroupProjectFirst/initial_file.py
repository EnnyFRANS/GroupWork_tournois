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
    def __init__(self):
        self.creature_level = 0

    # Make the enemy's level randomly chose base of the player's level
    def level_random(self, player_level):
        return random.randint(player_level -1, player_level +1)

creatures = Enemy()

# The 3 creatures for information
# creature_01 = ("Pikachu", "thunder", "kiss")
# creature_02 = ("Wyverne", "Storm", "Rest")
# creature_03 = ("Troll", "Axe", "Beer")

