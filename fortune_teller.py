# Example Mini-Project:
# THE MYSTICAL OCTOSPHERE! - Andrea Crain

# Type-your-question version

import random
import simplegui

def number_to_fortune(number):
    if number == 0:
        return "Yes, for sure!"
    elif number == 1:
        return "Probably yes."
    elif number == 2:
        return "Seems like yes..."
    elif number == 3:
        return "Definitely not!"
    elif number == 4:
        return "Probably not."
    elif number == 5:
        return "I really doubt it..."
    elif number == 6:
        return "Not sure, check back later!"
    elif number == 7:
        return "I really can't tell."
    else:
        return "Something was wrong with my input."

def mystical_octosphere(question):
    print "Your question was... " + question
    print "You shake the mystical octosphere."
    answer_number = random.randrange(0, 8)
    answer_fortune = number_to_fortune(answer_number)
    print "The cloudy liquid swirls, and a reply comes into view..."
    print "The mystical octosphere says... " + answer_fortune 
    print " "

    
# create frame   
frame = simplegui.create_frame("Mystical Octosphere", 50, 100)

# an input field:
frame.add_input("What is your question?", mystical_octosphere, 200)

frame.start()
