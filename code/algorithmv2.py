import random as r
import numpy as np
from RPS import Game

g = Game()
pick = ["Rock", "Paper", "Scissors"]
c = [[0, 1, 2],[1, 2, 0], [2, 0, 1]]
win = {0: 1, 1 : 2, 2 : 0}
propb_table = np.array([[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]])

class Mark2:

    def __init__(self):
        self.past_plays = [0,0,0,0]
        self.cplay = int
        self.current = int
        self.doubles = {}
        self.triples = {}
        self.fours = {}
        self.fives = {}
        self.sixes = {}
        self.games = 0
        self.counter = 1

    def push(self, x):
        if len(self.past_plays) < 6:
            self.past_plays.append(x)
        else:
            self.past_plays.pop(0)
            self.past_plays.append(x)

    def past_propb(self): #Make a dictionary of past propabilities
        if len(self.past_plays) >= 2:
            if tuple(self.past_plays[-2:]) in self.doubles:
                self.doubles[tuple(self.past_plays[-2:])] = self.doubles.get(tuple(self.past_plays[-2:])) + 1
            else:
                self.doubles[tuple(self.past_plays[-2:])] = 1

        if len(self.past_plays) >= 3:
            if tuple(self.past_plays[-3:]) in self.triples:
                self.triples[tuple(self.past_plays[-3:])] = self.triples.get(tuple(self.past_plays[-3:])) + 1
            else:
                self.triples[tuple(self.past_plays[-3:])] = 1

        if len(self.past_plays) >= 4:
            if tuple(self.past_plays[-4:]) in self.fours:
                self.fours[tuple(self.past_plays[-4:])] = self.fours.get(tuple(self.past_plays[-4:])) + 1
            else:
                self.fours[tuple(self.past_plays[-4:])] = 1

        if len(self.past_plays) >= 5:
            if tuple(self.past_plays[-5:]) in self.fives:
                self.fives[tuple(self.past_plays[-5:])] = self.fives.get(tuple(self.past_plays[-5:])) + 1
            else:
                self.fives[tuple(self.past_plays[-5:])] = 1

        if len(self.past_plays) >= 6:
            if tuple(self.past_plays[-6:]) in self.sixes:
                self.sixes[tuple(self.past_plays[-6:])] = self.sixes.get(tuple(self.past_plays[-6:])) + 1
            else:
                self.sixes[tuple(self.past_plays[-6:])] = 1
        
        return self.doubles, self.triples, self.fours, self.fives, self.sixes

    def current_propb(self): #Goes through the possible predictions from n(6) to n(2) or random using access function
        self.counter += 1

        if self.assess(5, self.past_plays, self.sixes) != None: #five depth
            #Iterate through other depths to see which one is best. 
            print("Five-depth!")
            print(self.sixes)
            return self.cplay
        elif self.assess(4, self.past_plays, self.fives) != None: #four depth
            #Iterate through other depths to see which one is best. 
            print("Four-depth!")
            print(self.fives)
            return self.cplay
        elif self.assess(3, self.past_plays, self.fours) != None: #three depth
            #Iterate through other depths to see which one is best. 
            print("Three-depth!")
            print(self.fours)
            return self.cplay
        elif self.assess(2, self.past_plays, self.triples) != None: #twp depth
            #Iterate through other depths to see which one is best. 
            print("Two-depth!")
            print(self.triples)
            return self.cplay
        elif self.assess(1, self.past_plays, self.doubles) != None: #single depth
            #Iterate through other depths to see which one is best. 
            print("One-depth!")
            print(self.doubles)
            return self.cplay
        else:
            print("I'm just guessing!")
            return r.randint(0,2)

    def assess(self, p: int, t: list, d: dict): #p is depth, t is last plays, d is correct dictionary
        if len(t) <= p:
            return None
        base = t[-p:]
        print(base)
        choices = []
        o = {}
        for i in [0,1,2]:
            base.append(i)
            choices.append(tuple(base))
            base.pop(-1)
        for choice in choices:
            if choice in d:
                o[choice] = o.get(tuple(choice))
        if len(o) == 0:
            return None
        self.cplay = win.get(max(zip(o.values(), o.keys()))[1][-1])
        return True
