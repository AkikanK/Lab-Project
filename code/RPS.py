import random as r
import time as t

choices = ["Rock", "Paper", "Scissors"]
wins = 0

class Game:

    def __init__(self):
        self.pscore = 0
        self.cscore = 0

    def gameplay(self, p1:int, p2:int):
        print(f"Player chose: {choices[p1]}")
        t.sleep(2)
        print(f"Computer chose: {choices[p2]}") 
        t.sleep(1)
        print("Result:")
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

    def score(self,add:int):
        if add == 1:
            self.pscore += 1
        if add == -1:
            self.cscore += 1

    def current(self):
        return [self.pscore, self.cscore]
    
if __name__ == "__main__":
    yeah = 0