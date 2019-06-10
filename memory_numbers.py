# implementation of card game - Memory

import simplegui
import random

cards = range(0,8)*2
random.shuffle(cards)
state = 0
card_posX = 0
card_posY = 65
count = 0
exposed = [False, False, False, False,False, False, False, False,
           False, False, False, False, False, False, False, False]
card_length = 100
card_width = 100


# helper function to initialize globals
def new_game():
    global state, exposed, count, turns
    state = 0
    random.shuffle(cards)
    exposed = [False, False, False, False,False, False, False, False,
           False, False, False, False, False, False, False, False]
    count = 0
    turns = "Turns = 0"
    label.set_text (str(turns))

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, first_card, second_card, count, turns, card_length
    if pos [1] < card_length:
        card_index = pos[0] // 100
    elif (pos [1] >= card_length) and (pos[1] < card_length* 2):
        card_index = (pos[0] // 100) + 4
    elif (pos [1] >= card_length * 2) and (pos[1] < card_length* 3):
        card_index = (pos[0] // 100) + 8 
    else:
        card_index = (pos [0] // 100) + 12   
    if state == 0:        
        if exposed[card_index] == False:
            exposed[card_index] = True
            first_card = card_index       
            state = 1
    elif state == 1:        
        if exposed [card_index] == False:
            exposed[card_index] = True
            second_card = card_index
            state = 2
            count += 1
            turns = "Turns = " + str(count)
            label.set_text (str(turns))
    elif state == 2: 
        if exposed [card_index] == False:
            if cards [first_card] != cards [second_card]:
                exposed [first_card] = False
                exposed [second_card] = False                
            if exposed [card_index] == False:
                exposed[card_index] = True
                first_card = card_index
            state = 1
  
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_posX, card_posY, card_length, card_width
    for card_index in range(len(cards)):  
        #draws numbers
        if exposed[card_index] == True: 
            if card_index < 4:
                card_posX = 40 + card_width * card_index
                card_posY = 15 + (card_length / 2)                              
            elif (card_index > 3) and (card_index < 8):
                card_posX = 40 + card_width *(card_index - 4)
                card_posY = 65 + card_length              
            elif (card_index > 7) and (card_index < 12):
                card_posX = 40 + card_width * (card_index - 8)
                card_posY = 65 + card_length *2                
            else:
                card_posX = 40 + card_width * (card_index - 12)
                card_posY = 65 + card_length *3
                
            canvas.draw_text(str(cards[card_index]), [card_posX,card_posY], 42, "White")                               
        #draws squares        
        else:
            if card_index < 4:
                card_posX = card_width * card_index
                card_posY = card_length
            elif (card_index > 3) and (card_index < 8):               
                card_posX = card_width*(card_index - 4)
                card_posY = card_length * 2
            elif (card_index > 7) and (card_index < 12):             
                card_posX = card_width * (card_index - 8) 
                card_posY = card_length *3
            else:
                card_posX = card_width * (card_index - 12)
                card_posY = card_length * 4 
            canvas.draw_polygon([[card_posX, card_posY], [card_posX, card_posY - card_length], 
                           [card_posX + card_width, card_posY - card_length ],
                           [card_posX + card_width, card_posY]], 1, 'Blue', "Turquoise")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 400, 400)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
