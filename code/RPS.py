import random as r
import time as t

choices = ["Rock", "Paper", "Scissors"]
wins = 0


class Game:

    def __init__(self): 
        self.result = 0 #Needed for the algorithm
        self.pscore = 0 #Counts Player wins
        self.cscore = 0 #Counts algorithm wins
        self.rounds = 0 #To count rounds for the UI

    def gameplay(self, p1:int, p2:int):
        self.rounds += 1
        match p1:
            case 0: #player chose Rock
                if p2 == 1:
                    self.score(-1)
                    return f"Loss! {choices[p2]} beats {choices[p1]}!"
                elif p2 == 2:
                    self.score(1)
                    return f"Win! {choices[p1]} beats {choices[p2]}!"
                else:
                    return "Tie!"
            case 1: #player chose Paper
                if p2 == 2:
                    self.score(-1)
                    return f"Loss! {choices[p2]} beats {choices[p1]}!"
                elif p2 == 0:
                    self.score(1)
                    return f"Win! {choices[p1]} beats {choices[p2]}!"
                else:
                    return "Tie!"
            case 2: #player chose Scissors
                if p2 == 0:
                    self.score(-1)
                    return f"Loss! {choices[p2]} beats {choices[p1]}!"
                elif p2 == 1:
                    self.score(1)
                    return f"Win! {choices[p1]} beats {choices[p2]}!"
                else:
                    return "Tie!"
            case _:
                None

    def score(self,add:int): #Updates the result and win counter
        if add == 1:
            self.result = 1
            self.pscore += 1
        if add == -1:
            self.result = -1
            self.cscore += 1

    def current(self):
        return [self.pscore, self.cscore]

