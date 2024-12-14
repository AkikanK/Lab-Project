import random as r
import time as t
from algorithmv3 import Mark3_nodepth1
from algorithmv4 import Mark4_nodepth1
from RPS import Game

pick = ["Rock", "Paper", "Scissors"]
    

if __name__ == "__main__": #Main gameplay loop
    M = Mark4_nodepth1() #Choose between Mark3 and Mark4
    g = Game()
    while True:
        test = int(input("Select length of test: (any number ofrepeats.)"))
        start_time = t.perf_counter()
        a = 0
        while test > a:
            player = r.randint(0,2)
            computer = M.current_propb() #Calculates the current probability for the algorithm
            M.current = computer
            M.push(player)
            M.past_propb()
            g.gameplay(player, computer) #Actual gameplay
            a += 1
        end_time = t.perf_counter()

        print(f"Final result of bot-test: \n Random-Number-Picker: {g.pscore}, Computer: {g.cscore}, You've played {M.counter} iterations! \n")
        print(f"time taken to execute: {end_time - start_time:.4f} seconds")
