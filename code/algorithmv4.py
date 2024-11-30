import random as r
import numpy as np

pick = ["Rock", "Paper", "Scissors"]
win = {0: 1, 1: 2, 2: 0}  # Used by the assess function to make a choice

class Mark4_nodepth1:
    def __init__(self):
        self.past_plays = []
        self.cplay = int
        self.current = int
        self.result = 0
        self.moves = {}  # Stores move history with counts
        self.counter = 0
        self.data = {"n5": 1, "n4": 0, "n3": 0, "n2": 0}  # Tracks efficiency of depth algorithms

    def push(self, x):
        if len(self.past_plays) < 6:
            self.past_plays.append(x)
        else:
            self.past_plays = self.past_plays[1:] + [x]

    def depth(self, n):  # Create dictionary of moves with length `n`
        return {i: self.moves.get(i) for i in self.moves if len(i) == n}

    def test(self, which: str, guess: int):  # Tests performance of a given depth algorithm
        from RPS import Game
        g = Game()
        try:
            g.gameplay(self.past_plays[-1], guess)
            self.data[which] += 1 if g.result == -1 else -1.5 if g.result == 1 else 0
        except TypeError:
            pass

    def past_propb(self):  # Updates move frequencies for different depths
        if len(self.past_plays) >= 3:
            for i in range(3, 6):
                key = tuple(self.past_plays[-i:])
                self.moves[key] = self.moves.get(key, 0) + 1
        return self.moves

    def current_propb(self):  # Decides current move based on most efficient depth algorithm
        self.counter += 1
        sorted_depths = sorted(self.data.keys(), key=self.data.get, reverse=True)
        for current in sorted_depths:
            depth = int(current[1])
            if (guess := self.assess(depth, self.past_plays, self.depth(depth + 1))) is not None:
                for i in range(2, 6):
                    self.test(f"n{i}", self.assess(i, self.past_plays, self.depth(i)))
                return guess

        return r.randint(0, 2)  # Play randomly if no algorithm can predict

    def assess(self, p: int, t: list, d: dict):  # Guesses next move based on past moves and depth
        if len(t) <= p:
            return None
        base = t[-p:]
        choices = [tuple(base + [i]) for i in range(3)]
        o = {choice: d.get(choice, 0) for choice in choices if choice in d}
        return None if not o else win[max(o, key=o.get)[-1]]

