
import random

name = input("What is your name?  ")
print("Hi {}! Welcome to the guessing game".format(name)+ "!"*len(name)+ "\nIn order to win the game you must guess a number from 1-10")
highscore = []

def start_game():
    solution = random.randrange(1,11)
    attempt_count = 1
    guess = 0
    
    
    while guess != solution:
        try:
            guess = int(input("Please guess a number:  "))
        
        except ValueError:
            attempt_count += 1
            print("Oh no! That's not a valid number.")
              
        else:    
            if guess < 1 or guess > 10:
                attempt_count += 1
                print("Oh no! That's out of range.")
            elif guess > solution:
                attempt_count += 1
                print("Oh no! The correct number is lower.")
            elif guess < solution:
                attempt_count += 1
                print("Oh no! The correct number is higher.")
       
    if guess == solution:
        attempt_count += 0
        highscore.append(attempt_count)
        start = input("You got it in {} attempt(s) {}!\nWould you like to try again? (Enter 'y' or 'n'):  ".format(attempt_count,name))
        if start.lower() == "y":
            print("Awesome! See if you can beat your highscore of {}.".format(min(highscore)))
            start_game()
        elif start != "y":
            print("Thanks for playing! Your highscore was {}.".format(min(highscore))) 
         
            
            
start_game()

    
    
