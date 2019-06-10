# implementation of card game - Memory

import simplegui
import random

# images
#dalmatian
image1 = simplegui.load_image ("https://thechive.files.wordpress.com/2017/05/dalmation.jpg?quality=85&strip=info&w=540")
#labrador
image2 = simplegui.load_image ("https://thechive.files.wordpress.com/2017/05/c-6ugyewaaeyvpi.jpg?quality=85&strip=info&w=600")
#retriver
image3 = simplegui.load_image ("https://thechive.files.wordpress.com/2017/05/golden-retriever.jpg?quality=85&strip=info&w=500")
#husky1
image4 = simplegui.load_image("https://thechive.files.wordpress.com/2017/05/husky.jpg?quality=85&strip=info&w=360")
#swedish dog
image5 = simplegui.load_image ("https://thechive.files.wordpress.com/2017/05/swedish-vallhund.jpg?quality=85&strip=info&w=600")
#rottweiler
image6 = simplegui.load_image("https://thechive.files.wordpress.com/2017/05/rottweiler-3.jpg?quality=85&strip=info&w=600")
#husky2
image7 = simplegui.load_image("https://thechive.files.wordpress.com/2017/05/c-2sbkfxoaamueq.jpg?quality=85&strip=info&w=540")
#pug
image8 = simplegui.load_image("https://thechive.files.wordpress.com/2017/05/pug.png?w=600&h=603")

image_list = [image1, image2, image3, image4, image5, image6, image7, image8, image1, 
              image2, image3, image4, image5, image6, image7, image8]

cards = range (0,8)* 2

random.shuffle(cards)
cards = image_list

#random.shuffle (image_list)
state = 0
card_posX = 0
card_posY = 0
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
    # game state logic here
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
            if  image_list[first_card] != image_list[second_card]:
                exposed [first_card] = False
                exposed [second_card] = False                
            if exposed [card_index] == False:
                exposed[card_index] = True
                first_card = card_index
            state = 1
    
                        
# cards are logically 100x100 pixels in size    
def draw(canvas):
    global card_posX, card_posY, card_length, card_width, image_size, image_center 
    for card_index in range(len(cards)):         
        if exposed[card_index] == True: 
            if image_list[card_index] == image1:
                image_size = [310,310]
                image_center = [310,220] 
            elif image_list[card_index] == image2:
                image_size = [411,312]
                image_center = [370,250]
            elif image_list[card_index] == image7:
                image_size = [300,254]
                image_center = [280,130]  
            else:
                image_size = [360,360]
                image_center = [(image_size [0]/2), (image_size [1] / 2)]
            if card_index < 4:
                center_destX = (card_width/2) + card_width * card_index
                center_destY = (card_length / 2)                              
            elif (card_index > 3) and (card_index < 8):
                center_destX = (card_width/2) + card_width *(card_index - 4)
                center_destY = (card_length / 2) + card_length              
            elif (card_index > 7) and (card_index < 12):
                center_destX =  (card_width/2) + card_width *(card_index - 8)
                center_destY = (card_length /2) + 2* card_length                
            else:
                center_destX = (card_width/2) + card_width * (card_index - 12)
                center_destY = (card_length /2)  + 3 * card_length
                
            canvas.draw_image(image_list[card_index],
                              image_center,
                              image_size,
                              (center_destX, center_destY), (card_width, card_length))                                      
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
