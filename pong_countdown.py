# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT/ 2]
ball_vel = [0,0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
count = 3

#timer handler
def tick():
    global count 
    count -= 1
    if count <= 0:
        timer.stop()   
        first_kick = random.choice ([RIGHT,LEFT])
        spawn_ball(first_kick)
    

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT/ 2]
    ball_vel = [0,0]
 
    if direction == RIGHT:          
        ball_vel[0] = random.randrange (120/60 ,240 / 60)
        ball_vel[1] = random.randrange (-180/60, -60 / 60)
    else:        
        ball_vel[0] = random.randrange (-240 / 60, -120/ 60)
        ball_vel[1] = random.randrange (-180 / 60, -60 / 60)
        
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel  # these are numbers
    global score1, score2, count  # these are ints
    score1 = 0
    score2 = 0
    count = 3
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    ball_pos = [WIDTH / 2, HEIGHT/ 2]
    ball_vel = [0,0]       
    timer.start()
      

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    #draw timer
    canvas.draw_text (str(count), (50,50), 12,"White" )
         
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos [0] += ball_vel[0]
    ball_pos [1] += ball_vel [1]
    
    # detemines if ball touches the top or bottom of the canvas
    if ball_pos [1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel [1]
    if ball_pos [1] >= (HEIGHT - BALL_RADIUS):
        ball_vel [1] = - ball_vel [1]
        
    # tests whether the ball collides with the left and right gutters  
    if ball_pos [0] <= BALL_RADIUS + PAD_WIDTH:   
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT - BALL_RADIUS)\
        and (ball_pos[1]<= paddle1_pos +HALF_PAD_HEIGHT + BALL_RADIUS):
            ball_vel [0] = - ball_vel [0] * 1.1  
        else:    
            spawn_ball (RIGHT)
            score2 += 1
    if ball_pos [0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT - BALL_RADIUS)\
        and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT + BALL_RADIUS):
            ball_vel [0] = - ball_vel [0]* 1.1
        else:
            spawn_ball (LEFT)
            score1 +=1
        
    # draw ball
    canvas.draw_circle(ball_pos, 20, 10, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen, determine whether paddle and ball collide 
    if (paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT)\
    and (paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel     
    if (paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT) \
    and (paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line ([PAD_WIDTH / 2,paddle1_pos - HALF_PAD_HEIGHT],
                      [PAD_WIDTH / 2, paddle1_pos + HALF_PAD_HEIGHT],PAD_WIDTH, "Red")
    canvas.draw_line([WIDTH - PAD_WIDTH / 2, paddle2_pos - HALF_PAD_HEIGHT],
                     [WIDTH - PAD_WIDTH / 2, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Blue")    
    
    # draw scores
    canvas.draw_text (str(score1), (200, 100), 24, "Green")
    canvas.draw_text (str(score2), (400, 100), 24, "Green")
    if score1 >= 10:
        canvas.draw_text ("Game  over", (220, 150), 30, "Red")
        canvas.draw_text ("Red player wins!", (200, 250), 30, "Red")
        ball_vel = [0,0]
    if score2 >= 10:
        canvas.draw_text ("Game  over", (220, 150), 30, "Blue")
        canvas.draw_text("Blue player wins!", (200, 250), 30, "Blue")
        ball_vel = [0,0]

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3
    if key == simplegui.KEY_MAP ["w"]:
        paddle1_vel -= acc
    if key == simplegui.KEY_MAP ["s"]:
        paddle1_vel += acc
    if key == simplegui.KEY_MAP ["up"]:
        paddle2_vel -= acc
    if key == simplegui.KEY_MAP ["down"]:
        paddle2_vel += acc
        
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 0
    if key == simplegui.KEY_MAP ["w"]:
        paddle1_vel = 0 
    if key == simplegui.KEY_MAP ["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP ["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP ["down"]:
        paddle2_vel = 0


# create frame and register handlers
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button ("Start", new_game)
timer = simplegui.create_timer(1000, tick)


# start frame
frame.start()
