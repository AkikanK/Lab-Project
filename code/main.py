import random as r
import time as t
import numpy as np
from RPS import Game
from algorithmv2 import Mark1

pick = ["Rock", "Paper", "Scissors"]
    

if __name__ == "__main__":
    M = Mark1()
    g = Game()
    test = input("Want to play? Y/N")
    if test == "n":
        print("'Kay bye!")
        False
        
    while True:
        player = int(input("Rock (0), Paper (1), or Scissors (2)? \n"))
        computer = M.current_propb()
        M.current = computer
        print(g.gameplay(player, computer))
        print(f"Current Score: Player: {g.pscore}, Computer: {g.cscore}, You've played {M.counter} rounds!")
        M.push(player)
        M.past_propb()