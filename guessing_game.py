"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

            
def start_game():
    name = input("Hi there \U0001F44B, welcome to the Number Guessing Game! \U0001F3AE What is your name?  ") 
    print("Let's get started {}!".format(name))
    
    number = random.randint(1,10)
    
    while True: 
        try: 
            guess = input("Pick a random number from 1 to 10:  ")
            guess = int(guess) 
            break
        except ValueError:
            print("Oops! You need to type in the numerical value of any number from 1 to 10. Try again")
            
        
    
    while guess != number:
        if guess > number:
            print("It's lower")
            guess = input("Guess again  ")
            guess = int(guess)
        else:
            print("It's higher")
            guess = input("Guess again  ")
            guess = int(guess)
        
    print("Got it")
    print("Congratulations {}, you have guessed the correct number! Way to go smarty pants! The game is now over.".format(name))        
   
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()