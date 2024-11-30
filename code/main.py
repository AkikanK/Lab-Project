import random as r
import time as t
import numpy as np
from algorithmv3 import Mark3_nodepth1
from RPS import Game

pick = ["Rock", "Paper", "Scissors"]
    

if __name__ == "__main__": #Main gameplay loop
    M = Mark3_nodepth1()
    g = Game()
    test = input("Want to play? Y/N")
    if test == "n":
        print("'Kay bye!")
        False
    while True:
        player = int(input("Rock (0), Paper (1), or Scissors (2)? \n"))
        if player not in range(0,3):
            player = int(input("Rock (0), Paper (1), or Scissors (2)? \n"))
        computer = M.current_propb() #Calculates the current probability for the algorithm
        M.current = computer
        M.push(player)
        M.past_propb()
        print(f"Player chose: {pick[player]}")
        t.sleep(2) #Pause for dramatic effect
        print(f"Computer chose: {pick[computer]}") 
        t.sleep(1) #Pause for dramatic effect Part 2
        print("Result:")
        print(g.gameplay(player, computer)) #Actual gameplay
        print(f"Current Score: Player: {g.pscore}, Computer: {g.cscore}, You've played {M.counter} rounds! \n")
        print(M.data)