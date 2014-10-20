
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

secret_number=0
n=0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,n
    secret_number=random.randrange(0,100)
    low=0
    high=99
    n=int(math.ceil(math.log((high-low+1),2)))
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses",n
    print ""
    


# define event handlers for control panel
def range100():
    global secret_number,n
    secret_number=random.randrange(0,100)
    low=0
    high=99
    n=int(math.ceil(math.log((high-low+1),2)))
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses",n
    print ""
    

def range1000():
    global secret_number,n
    secret_number=random.randrange(0,1000)
    low=0
    high=999
    n=int(math.ceil(math.log((high-low+1),2)))
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses",n
    print ""
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number,n
    number=int(guess)
    print "Guess was",number
    if n>0:
            if(secret_number > number):
                n=n-1
                print "Number of remaining guesses",n
                print "Higher"     
                print ""
            elif(secret_number < number):
                n=n-1
                print "Number of remaining guesses",n
                print "Lower"     
                print ""
            else:
                n=n-1
                print "Correct"     
                print ""
                new_game()
    else:
            print "Lost the game"
            print ""
            new_game()
    
    

    
# create frame
f=simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range in (0,100]",range100,200)
f.add_button("Range in (0,1000]",range1000,200)
f.add_input("Enter the number",input_guess,200)

# call new_game 
new_game()


