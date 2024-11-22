import random as r
import numpy as np

pick = ["Rock", "Paper", "Scissors"]
c = [[0, 1, 2],[1, 2, 0], [2, 0, 1]]
win = {0: 2, 1 : 0, 2 : 1}
propb_table = np.array([[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]])

class Mark3_nodepth1:

    def __init__(self):
        self.past_plays = []
        self.cplay = int
        self.current = int
        self.result = 0
        self.triples = {}
        self.fours = {}
        self.fives = {}
        self.sixes = {}
        self.counter = 0
        self.data = {"n2":0, "n3":0, "n4":0, "n5": 1}

    def push(self, x):
        if len(self.past_plays) < 6:
            self.past_plays.append(x)
        else:
            self.past_plays.pop(0)
            self.past_plays.append(x)

    def test(self, which: str, guess:int):
        from RPS import Game
        g = Game()
        try:
            g.gameplay(self.past_plays[-1], guess)
            if g.result == -1:
                self.data[which] = self.data.get(which) +1
            return
        except TypeError:
            return
        
    def past_propb(self): #Make a dictionary of past propabilities
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
        
        return self.triples, self.fours, self.fives, self.sixes

    def current_propb(self): #For now goes from longest to shortest, will add switch function later
        self.counter += 1
        sorted_depths = sorted(self.data.keys(), key=lambda k: self.data[k], reverse=True)
        for current in sorted_depths:
            match current:
                case "n5":
                    if self.assess(5, self.past_plays, self.sixes) != None: #five depth
                        print("Five-depth!")
                        self.test("n5",self.assess(5, self.past_plays, self.sixes))
                        self.test("n4",self.assess(4, self.past_plays, self.fives))
                        self.test("n3",self.assess(3, self.past_plays, self.fours))
                        self.test("n2",self.assess(2, self.past_plays, self.triples))
                        return self.assess(5, self.past_plays, self.sixes)
                    
                case "n4":
                    if self.assess(4, self.past_plays, self.fives) != None: #four depth
                        print("Four-depth!")
                        self.test("n5",self.assess(5, self.past_plays, self.sixes))
                        self.test("n4",self.assess(4, self.past_plays, self.fives))
                        self.test("n3",self.assess(3, self.past_plays, self.fours))
                        self.test("n2",self.assess(2, self.past_plays, self.triples))
                        return self.assess(4, self.past_plays, self.fives)

                case "n3":
                    if self.assess(3, self.past_plays, self.fours) != None: #three depth
                        print("Three-depth!")
                        self.test("n5",self.assess(5, self.past_plays, self.sixes))
                        self.test("n4",self.assess(4, self.past_plays, self.fives))
                        self.test("n3",self.assess(3, self.past_plays, self.fours))
                        self.test("n2",self.assess(2, self.past_plays, self.triples))
                        return self.assess(3, self.past_plays, self.fours)

                case "n2":
                    if self.assess(2, self.past_plays, self.triples) != None: #twp depth
                        print("Two-depth!")
                        self.test("n5",self.assess(5, self.past_plays, self.sixes))
                        self.test("n4",self.assess(4, self.past_plays, self.fives))
                        self.test("n3",self.assess(3, self.past_plays, self.fours))
                        self.test("n2",self.assess(2, self.past_plays, self.triples))
                        return self.assess(2, self.past_plays, self.triples)

        print("I'm just guessing!")
        return r.randint(0,2)
    

    def assess(self, p: int, t: list, d: dict): #p is depth, t is last plays, d is correct dictionary
        if len(t) <= p:
            return None
        base = t[-p:]
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
        return win[(max(zip(o.values(), o.keys()))[1][-1])]
