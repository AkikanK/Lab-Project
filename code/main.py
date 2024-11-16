import random as r
import time as t
import numpy as np
from RPS import Game


pick = ["Rock", "Paper", "Scissors"]
transitions = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"]]
propb_table = np.array([[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]])

class Mark1:

    def __init__(self):
        self.past_plays = []
        self.cplay = int
        self.current = int

    def push(self, x):
        if len(self.past_plays) < 5:
            self.past_plays.append(x)
        else:
            self.past_plays.pop(0)
            self.past_plays.append(x)

    def current_propability(self): #Store the current values
        
        self.cplay = r.randint(0,2)
        return self.cplay

        """if len(self.past_plays) == 0:
            self.cplay = r.randint(0,2)
            return self.cplay

        else:
            match self.current:
                case 0:

                    return 0
                
                case 1:

                    return 1
                
                case 2:

                    return 2"""


    #Should take in the first value and then adjust the propabilities based on what is going on.

    def past_propb(): #Make a dictionary of past propabilities
        return None 

    #Should store previous tables to evaluate propabilities further

    def assess(): #Will take a look at the past few plays to consider what to do.
        return None
    
    

if __name__ == "__main__":
    
    print(propb_table)
    M = Mark1()
    g = Game()
    while True:
        test = input("Want to play? Y/N")
        if test == "n":
            print("'Kay bye!")
            break
        player = int(input("Rock (0), Paper (1), or Scissors (2)? \n"))
        computer = M.current_propability()
        M.current = computer
        print(g.gameplay(player, computer))
        print(f"Current Score: Player: {g.pscore}, Computer: {g.cscore}")
        M.push(M.current)
        print(propb_table)
        print(M.current)
        print(M.past_plays)