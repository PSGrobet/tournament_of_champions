import random
import time


class Battle:
    def __init__(self, fighters):
        self.fighters = fighters

    def choose_oponents(self):
        return random.sample(self.fighters, 2)
    
    def execute_turn(self, attacker, defender):
        attack = attacker.get_attack()
        defense = defender.get_defense()
        defender.health -= (attack - defense) if (attack - defense) > 0 else 0

        print(f"{attacker.name} attacks {defender.name} with a strong punch of {attack} damage!")
        time.sleep(0.5)
        print(f"{defender.name} defends and takes {attack - defense} damage")
        
    
    
    def print_stats(self, oponents):
        print(f"\033[93m{oponents[0].name.upper() }[ {oponents[0].health} ]\t{oponents[1].name.upper()} [ {oponents[1].health} ]\033[0m")
        

    def fight_on(self, fighter_a, fighter_b):
        return fighter_a.is_alive() & fighter_b.is_alive()
    
    def get_winner(self, oponents):
        winner = oponents[0] if oponents[1].health <= 0 else oponents[1]
        return f"{winner.name} WINS THIS MATCH!"
        
        
    
