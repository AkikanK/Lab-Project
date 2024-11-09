import random as r
import time as t

choices = ["Rock", "Paper", "Scissors"]
wins = 0

def gameplay(p1:int, p2:int):
    print(f"Player chose: {choices[p1]}")
    t.sleep(3)
    print(f"Computer chose: {choices[p2]}") 
    t.sleep(1)
    print("Result:")
    match p1:
        case 0: #player chose Rock
            if p2 == 1:
                return f"Loss! {choices[p2]} beats {choices[p1]}!"
            elif p2 == 2:
                return f"Win! {choices[p1]} beats {choices[p2]}!"
            else:
                return "Tie!"
        case 1: #player chose Paper
            if p2 == 2:
                return f"Loss! {choices[p2]} beats {choices[p1]}!"
            elif p2 == 0:
                return f"Win! {choices[p1]} beats {choices[p2]}!"
            else:
                return "Tie!"
        case 2: #player chose Scissors
            if p2 == 0:
                return f"Loss! {choices[p2]} beats {choices[p1]}!"
            elif p2 == 1:
                return f"Win! {choices[p1]} beats {choices[p2]}!"
            else:
                return "Tie!"

if __name__ == "__main__":
    while True:
        test = input("Want to play? Y/N")
        if test == "n":
            print("'Kay bye!")
            break
        player = int(input("Rock (0), Paper (1), or Scissors (2)? \n"))
        computer = r.randint(0,2)
        print(gameplay(player, computer))