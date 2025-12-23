import random
import time
from boxer import Boxer
from battle import Battle

"""
TOURNAMENT OF CHAMPIONS
A little "game" where two random fighters fight using their skills and special abilities.
The game selects two fighters and the match starts. The fighters use their unique stats 
and special abilities until one wins.
"""

def print_slow(message, pause_time=0.1):
    for c in message:
        print(c, end='', flush=True)
        time.sleep(pause_time)
    print()
        

def main():

    fighters = [
        Boxer("Carlos", 20, 5, 5),
        Boxer("Donny", 22, 4, 4),
        Boxer("Sam", 18, 6, 5),
        Boxer("Johnny", 20, 6, 3),
        Boxer("Daniel", 24, 2, 1)
    ]

    fight = Battle(fighters)
    oponents = fight.choose_oponents()
    
    print_slow("Welcome to TOURNAMENT OF CHAMPIONS!")
    time.sleep(1)
    print_slow(f"Tonight, {oponents[0].name} will fight {oponents[1].name}")
    time.sleep(1)
    print("\nFIGHT!")

    r = 0

    while fight.fight_on(oponents[0], oponents[1]):
        r += 1
        print("=" * 30)
        print(f"Round {r}")
        print("=" * 30)

        fight.execute_turn(oponents[0], oponents[1])

        if not oponents[0].is_alive() or not oponents[1].is_alive():
            break
        
        fight.execute_turn(oponents[1], oponents[0])
        if not oponents[0].is_alive() or not oponents[1].is_alive():
            break
        fight.print_stats(oponents)

    print("=" * 30)
    print_slow(fight.get_winner(oponents))
    

main()