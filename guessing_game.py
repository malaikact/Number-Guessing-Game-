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
   
start_game()