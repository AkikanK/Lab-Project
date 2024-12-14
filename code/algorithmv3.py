import random as r

pick = ["Rock", "Paper", "Scissors"]
win = {0: 1, 1 : 2, 2 : 0} #Used by the assess function to make a choice

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
        self.data = {"n5": 1, "n4":0, "n3":0, "n2":0} #Keeps count of which depth-algorithm is currently the most efficient, and uses that one.
        self.identity = {2: self.triples, 3: self.fours, 4: self.fives, 5: self.sixes}

    def push(self, x):
        if len(self.past_plays) < 6:
            self.past_plays.append(x)
        else:
            self.past_plays.pop(0)
            self.past_plays.append(x)

    def test(self, which: str, guess:int): #Tests how an algorithm would have performed IF it was played, checked for each depth each time.
        from RPS import Game
        g = Game()
        try:
            g.gameplay(self.past_plays[-1], guess)
            if g.result == -1:
                self.data[which] = self.data.get(which) +1
            if g.result == 1:
                self.data[which] = self.data.get(which) -1.5
            return
        except TypeError:
            return
        
    def past_propb(self): #Makes a dictionary for each past move length (Different depths)
        try:
            for i in range(2, 6):  # For depths 3 to 6
                if len(self.past_plays) >= (i+1):
                    past_tuple = tuple(self.past_plays[-(i+1):])
                    if past_tuple in self.identity[i]:
                        self.identity[i][past_tuple] += 1
                    else:
                        self.identity[i][past_tuple] = 1
                else:
                    pass
        except TypeError:
            pass

        return self.triples, self.fours, self.fives, self.sixes

    def current_propb(self): #For now goes from longest to shortest, will add switch function later
        self.counter += 1
        sorted_depths = sorted(self.data.keys(), key=lambda k: self.data[k], reverse=True)
        for current in sorted_depths:
            match current:
                case "n5":
                    if self.assess(5, self.past_plays, self.sixes) != None: #five depth
                        for n in range(2,6):
                            self.test(f"n{n}",self.assess(n, self.past_plays, self.identity.get(n)))
                        return self.assess(5, self.past_plays, self.sixes)
                    
                case "n4":
                    if self.assess(4, self.past_plays, self.fives) != None: #four depth
                        for n in range(2,6):
                            self.test(f"n{n}",self.assess(n, self.past_plays, self.identity.get(n)))
                        return self.assess(4, self.past_plays, self.fives)

                case "n3":
                    if self.assess(3, self.past_plays, self.fours) != None: #three depth
                        for n in range(2, 6):
                            self.test(f"n{n}", self.assess(n, self.past_plays, self.identity.get(n)))

                        return self.assess(3, self.past_plays, self.fours)

                case "n2":
                    if self.assess(2, self.past_plays, self.triples) != None: #twp depth
                        for n in range(2,6):
                            self.test(f"n{n}",self.assess(n, self.past_plays, self.identity.get(n)))
                        return self.assess(2, self.past_plays, self.triples)

        return r.randint(0,2) #If no algorithm is able to make a guess, we play a random
    

    def assess(self, p: int, t: list, d: dict): #p is depth, t is last plays, d is correct dictionary, it goues through the list up to t amount of plays, and then guesses move for t+1
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
