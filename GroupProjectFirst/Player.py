# Create a player's class
class Player:

    def __init__(self, level, health):
        #self.name = input("Hello! What is your name?")
        self.level = level
        self.health = health

    def level_up(self):
        self.level += 1

    def loose_health(self):
        self.health -= 1
