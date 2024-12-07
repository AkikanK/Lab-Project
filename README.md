# Lab-Project
**Basic Information:**
My lab project is a five-level Markov Chain algorithm to compete against human-players in a game of Rock-Paper-Scissors.
It is an experimental algorithm based on this research paper: https://arxiv.org/pdf/2003.06769. It uses a dictionary and the basic theory of Markov Chains as its core.
!SEE NOTES REGARDING THE ADDITION OF A NEW VERSION OF THE ALGORITHM!


**Getting Started:**
The program requires all files found in the 'code'-folder to function, as well as all the dependencies mentioned in the requirements.txt document.

Once the files have all been downloaded into the same folder, the program is run and can be tested from the main.py file or the bottest.py file. 
I have included initialisation code, so the program will run both in terminal or any python-supporting software of your choosing.


**Using the program:**

For Playing:
The main.py contains code which ensures that all the proper events occur within the algorithm file (do not modify it).
To start, simply run the code in the main.py document..
You are placed in the main gameplay loop of a game of Rock-Paper-Scissors. After each choice, you will see the result, and can play again by pressing the button below the choices.
In the background, the algorithm (which I have annotated more in my testing document as well as the code in algorithmv3.py) learns to play based on your moves,
and (hopefully) will improve and become more accurate the longer that you play. 

For Bot-testing:
The bottest.py file can be used to test the algorithm against a random number generator. My own tests are in the tests document, but if you want to compare the results you get with mine, 
feel free to try it!
When you run the code, you are asked to enter an integer (any integer) without any formatting.
The code will run and return the wins and losses of the random number generator vs the algorithm. Afterwards, you can enter more values, if you'd like to try adding on to the previously run round.

**Notes:**

After feedback from Week 4, I have created two versions of the algorithm (v3 and v4), you can read about the differences in the test documents, or by seeing the code. You can switch between the two algorithms (function the exact same way) by choosing between them in the imports.
As Rock-Paper-Scissors is still based on making (educated) guesses, and humans can be unpredictable, the algorithm may play terribly in one game,
and then be unbeatable in another. The algorithm does not measure your level of ability within the game, but is simply programmed to make educated guesses.
From personal experience, I would recommend to play at least a few games of 50 rounds to develop a full view of the accuracy of the algorithm.
After week 5, the game now has a more intuitive and user friendly UI. Enjoy! :)
