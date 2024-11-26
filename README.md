# Lab-Project
**Basic Information:**
My lab project is a five-level Markov Chain algorithm to compete against human-players in a game of Rock-Paper-Scissors.
It is an experimental algorithm based on this research paper: https://arxiv.org/pdf/2003.06769. It uses a dictionary and the basic theory of Markov Chains as its core.


**Getting Started:**
The program requires all three files found in the 'data'-folder to function, as well as all the dependencies mentioned in the requirements document.

Once the files have all been downloaded into the same folder, the program is run and can be tested from the main.py file. 
I have included initialisation code, so the program can be run both in terminal or any python-supporting software of your choosing.


**Using the program:**
The main.py contains code which ensures that all the proper events occur within the algorithm file (do not modify it).
To start, simply run the code in the main.py document.
The player is first prompted to press any other key except e (Exit).
Afterwards you are placed in the main gameplay loop of picking between three integers, which correspond to choices in a game of Rock-Paper-Scissors:
0 = Rock, 1 = Paper, 2 = Scissors.
In the background, the algorithm (which I have annotated more in my testing document as well as the code in algorithmv3.py) learns to play based on your moves,
and (hopefully) will improve and become more accurate the longer that you play. 


**Notes:**

As Rock-Paper-Scissors is still based on making (educated) guesses, and humans can be unpredictable, the algorithm may play terribly in one game,
and then be unbeatable in another. The algorithm does not measure your level of ability within the game, but is simply programmed to make educated guesses.
From personal experience, I would recommend to play at least a few games of 50 rounds to develop a full view of the accuracy of the algorithm.
