import random as r
import time as t
import numpy as np
from RPS import Game
from algorithm import Mark1

pick = ["Rock", "Paper", "Scissors"]

#On average 3250 ties, 3400 wins, 3350 losses, dose not do that well against a random number generator.

if __name__ == "__main__":
    counter = 1
    M = Mark1()
    g = Game()
    while True:
        player = 0
        computer = M.current_probability()
        M.current = computer
        print(g.gameplay(1, computer))
        print(f"Current Score: Player: {g.pscore}, Computer: {g.cscore}")
        M.push(player)
        print(f"Games played: {counter}")
        counter += 1
        if counter > 100:
            print(100 - g.pscore - g.cscore) 
            break