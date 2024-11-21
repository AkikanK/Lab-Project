import random as r
import time as t
import numpy as np
from RPS import Game
from algorithm import Mark1

pick = ["Rock", "Paper", "Scissors"]
    

if __name__ == "__main__":
    counter = 1
    M = Mark1()
    g = Game()
    while True:
        test = input("Want to play? Y/N")
        if test == "n":
            print("'Kay bye!")
            break
        player = int(input("Rock (0), Paper (1), or Scissors (2)? \n"))
        computer = M.current_propb()
        M.current = computer
        print(g.gameplay(player, computer))
        print(f"Current Score: Player: {g.pscore}, Computer: {g.cscore}")
        M.push(player)
        M.past_propb()
        print(M.counter)