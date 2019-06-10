# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num = 100
attempt = 7

# helper function to start and restart the game
def new_game():
    """ Starts a new game"""
    global num, attempt, secret_number
    secret_number = random.randrange (0,num)
    if num == 100:
        attempt = 7
    if num == 1000:
        attempt = 10
    print " "
    print "New game. Range is from 0 to", num
    print "Number of remaining guesses is", attempt    
    return secret_number, attempt
      

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, attempt, num
    num = 100
    attempt = 7
    new_game ()

    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, attempt, num
    num = 1000
    attempt = 10
    new_game ()
    
    
def input_guess(guess):
    global attempt, secret_number, num   
    guess = int(guess)
    print " "
    print "Your guess was", int(guess)
    if guess < secret_number:
        attempt -= 1
        print "Higher" 
        print "Number of remaining guesses is", attempt 
        if attempt == 0:
            print "Game over: you lost. Try again"
            print "Secret number was", secret_number
            new_game()
    elif guess > secret_number:
        attempt -= 1
        print "Lower"
        print "Number of remaining guesses is", attempt 
        if attempt == 0:
            print "Game over: you lost. Try again"
            print "Secret number was", secret_number 
            new_game()
    elif guess == secret_number:
        print "Correct!" 
        new_game()
    else:
        print " Error: choose from the range"
         
    
# create frame
frame = simplegui.create_frame("Guess the number", 250, 250)

# register event handlers for control elements and start frame
frame.add_input('Type in the number', input_guess, 150)
frame.add_button('Range is [0, 100)', range100, 130)
frame.add_button('Range is [0, 1000)', range1000, 130)
frame.start()

#call new_game 
new_game()

