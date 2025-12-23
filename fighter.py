import random

class Fighter:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.health > 0
    
    def get_defense(self):
        return random.randrange(0, self.defense)

    def get_attack(self):
        return random.randrange(self.attack - 2, self.attack + 2)

    