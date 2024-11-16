import numpy as np
import random as r

pick = ["Rock", "Paper", "Scissors"]
transitions = [["RR", "RP", "RS"], ["PR", "PP", "PS"], ["SR", "SP", "SS"]]
starting_propb = np.array([[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]])

class Mark1:

    past_plays = []

    def current_propability(): #Store the current values
        return None

    def past_propb(): #Make a dictionary of past propabilities
        return None 

    def assess(): #Will take a look at the past few plays to consider what to do.
        return None