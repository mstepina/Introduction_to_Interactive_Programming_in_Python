# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: choose rock, Spock, paper, lizard or scissors"

# convert number to a name 
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: numbers should be from 0 to 4"
            
    
import random

def rpsls(player_choice): 
    print " "    
    print "Player chooses " + player_choice
    
    # convert the player's choice to player_number
    player_number = name_to_number (player_choice)
    
    # compute random guess for comp_number
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice
    comp_choice = number_to_name(comp_number)
       
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    
    # determine winner, print winner message
    if (difference == 1) or (difference == 2):
        print "Computer wins!"
    elif (difference == 3) or (difference == 4):
        print "Player wins!"
    elif difference == 0:
        print "Player and computer tie!"
    else:
        print "Error: try again"

    
# tests 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
