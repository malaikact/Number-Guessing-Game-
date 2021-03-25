import random          
def start_game():
    score = 0 
    name = input("Hi there \U0001F44B, welcome to the Number Guessing Game! \U0001F3AE What is your name?  ") 
    print("The highscore is {}, let's see if you can beat it.".format(score))
    print("Let's get started {}!".format(name))
    
    number = random.randint(1,10)
    
    guess = guess_again(0)
    attempts = 1

    while guess != number:
        if guess > 10 or guess < 0:
            print("Oops! That number is not within the range. Try again")
            attempts +=1
            guess = guess_again(guess)
        elif guess > number:
            print("It's lower")
            attemps +=1
            guess = guess_again(guess)
        else:
            print("It's higher")
            guess = guess_again(guess)

    if attempts < score: 
        score = attempts
    elif score == 0:
        score += attempts

    print("Got it!")
    print("Congratulations {}, you have guessed the correct number! It only took you {} attempts and your score is now {}. Way to go smarty pants! The game is now over.".format(name, attempts, score))        
    play_again = input("Would you like to play again? (Yes/No)")
    if play_again.lower() == "yes":
        start_game()
    elif play_again.lower() == "no":
        print("Thanks for playing with us {}. See you next time!".format(name))
   

def guess_again(guess):
    while True: 
        try: 
            guess = int(input("Pick a random number from 1 to 10:  "))
            break
        except ValueError:
            print("Oops! You need to type in the numerical value of any number from 1 to 10. Try again")
            continue
    return guess 

start_game()