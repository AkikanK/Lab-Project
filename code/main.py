import random as r
import time as t
import numpy as np
from algorithmv3 import Mark3_nodepth1
from RPS import Game

pick = ["Rock", "Paper", "Scissors"]
    

if __name__ == "__main__":
    M = Mark3_nodepth1()
    g = Game()
    test = input("Want to play? Y/N")
    if test == "n":
        print("'Kay bye!")
        False
    while True:
        player = int(input("Rock (0), Paper (1), or Scissors (2)? \n"))
        M.push(player)
        computer = M.current_propb()
        M.past_propb()
        M.current = computer
        print(f"Player chose: {pick[player]}")
        t.sleep(2)
        print(f"Computer chose: {pick[computer]}") 
        t.sleep(1)
        print("Result:")
        print(g.gameplay(player, computer))
        print(f"Current Score: Player: {g.pscore}, Computer: {g.cscore}, You've played {M.counter} rounds!")
        print(M.data)