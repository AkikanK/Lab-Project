from tkinter import *
import random
import time as t
import numpy as np
from algorithmv3 import Mark3_nodepth1
from RPS import Game

M = Mark3_nodepth1()
g = Game()
# Create Object
root = Tk()
 
# Set geometry
root.geometry("800x300")
 
# Set title
root.title("Rock Paper Scissor Game")
 
# Computer Value
choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
# Reset The Game
 
 
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")
    l4.config(text="")
 
# Disable the Button
 
 
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 
# If player selected rock
 
 
def isrock():
    c_v = M.current_propb() #Calculates the current probability for the algorithm
    player = 0
    M.current = c_v
    g.gameplay(player, c_v)
    if c_v == 0:
        match_result = "Match Draw"
    elif c_v == 2:
        match_result = f"Player Win, Wins: {g.pscore}, Losses: {g.cscore}"
    else:
        match_result = f"Computer Win, Wins: {g.pscore}, Losses: {g.cscore}"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=choices.get(c_v))
    M.push(player)
    M.past_propb()
    button_disable()
 
# If player selected paper
 
 
def ispaper():
    c_v = M.current_propb() #Calculates the current probability for the algorithm
    player = 1
    M.current = c_v
    g.gameplay(player, c_v)
    if c_v == 1:
        match_result = "Match Draw"
    elif c_v == 2:
        match_result = f"Computer Win, Wins: {g.pscore}, Losses: {g.cscore}"
    else:
        match_result = f"Player Win, Wins: {g.pscore}, Losses: {g.cscore}"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=choices.get(c_v))
    M.push(player)
    M.past_propb()
    button_disable()
 
# If player selected scissor
 
 
def isscissor():
    c_v = M.current_propb() #Calculates the current probability for the algorithm
    player = 2
    M.current = c_v
    g.gameplay(player, c_v)
    if c_v == 0:
        match_result = f"Computer Win, Wins: {g.pscore}, Losses: {g.cscore}"
    elif c_v == 2:
        match_result = "Match Draw"
    else:
        match_result = f"Player Win, Wins: {g.pscore}, Losses: {g.cscore}"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=choices.get(c_v))
    M.push(player)
    M.past_propb()
    button_disable()
 
 
# Add Labels, Frames and Button
Label(root,
      text="Rock Paper Scissor",
      font="normal 20 bold",
      fg="blue").pack(pady=10)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text="Player              ",
           font=10)
 
l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold")
 
l3 = Label(frame, text="Computer", font=10)
 
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
 
l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="white",
           width=30,
           borderwidth=2,
           relief="solid")
l4.pack(pady=10)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text="Rock",
            font=10, width=7,
            command=isrock)
 
b2 = Button(frame1, text="Paper ",
            font=10, width=7,
            command=ispaper)
 
b3 = Button(frame1, text="Scissor",
            font=10, width=7,
            command=isscissor)
 
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)
 
Button(root, text="Reset Game",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)
 
# Execute Tkinter
root.mainloop()
