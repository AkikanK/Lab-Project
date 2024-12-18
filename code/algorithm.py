import random as r
import numpy as np


pick = ["Rock", "Paper", "Scissors"]
c = [[0, 1, 2],[1, 2, 0], [2, 0, 1]]
propb_table = np.array([[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]])

class Mark1:

    def __init__(self):
        self.past_plays = []
        self.cplay = int
        self.current = int
        self.predict = {}
        self.games = 0
        self.counter = 1

    def push(self, x):
        if len(self.past_plays) < 5:
            self.past_plays.append(x)
        else:
            self.past_plays.pop(0)
            self.past_plays.append(x)

    def past_propb(self): #Make a dictionary of past propabilities
        if self.games == 4:
            if tuple(self.past_plays) in self.predict:
                self.predict[tuple(self.past_plays)] = self.predict.get(tuple(self.past_plays)) + 1
            else:
                self.predict[tuple(self.past_plays)] = 1
            self.games = 0
            print(self.games)
            return self.predict
        self.games += 1
        return f"{self.games} games since updated prediction!"

    def current_propb(self): #Pick the best value by accessing the 'assess' function
        self.counter += 1
        if len(self.past_plays) >= 5:
                p = self.past_plays[-1]
                choices = self.assess(p, propb_table[p],self.predict)
                locked = propb_table[p]
                lock_in = int(np.argmin(locked))

                return c[p][lock_in]

        #picks randomly until we have some values to use! 

        return r.randint(0,2)

    def assess(self, p: int, t: list, d: dict): #Calculates new values for probabilities for the current row at play

        rocks = 0.000001
        papers = 0.000001
        scissors = 0.000001
        for k in d:
            for i in range(len(k)):
                if k[i] == 0: 
                    rocks += 1
                elif k[i] == 1:
                    papers += 1
                elif k[i] == 2:
                    scissors += 1
                i += 1
            m = d.get(k)
            rocks*m and papers*m and scissors*m

        """if self.current == 0:
            rocks += 1
        elif self.current == 1:
            papers += 1
        else:
            scissors += 1"""
        # I will maybe implement a way for the algorithm to avoid repeating answers.

        match p:
            case 0:
                t[0] = t[0] * rocks - t[0]/5
                t[1] = t[1] * papers - t[1]/2 -1
                t[2] = t[2] * scissors - t[2]/4
            case 1:
                t[0] = t[0] * papers - t[0]/5
                t[1] = t[1] * scissors - t[1]/2 -1
                t[2] = t[2] * rocks - t[2]/4
            case 2:
                t[0] = t[0] * scissors - t[0]/5
                t[1] = t[1] * rocks - t[1]/2 -1
                t[2] = t[2] * papers - t[2]/4


        t = t / np.sum(t)

        return t