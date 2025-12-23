from fighter import Fighter

class Boxer(Fighter):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    