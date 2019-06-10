# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0  
a = 0
b = 0
c = 0 
d = 0
count1 = 0
count2 = 0
running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a,b,c,d
    a = t // 10 // 60
    b = ((t // 10)% 60) // 10
    c = ((t // 10) % 60) % 10
    d = t % 10
    return str (a) + ":" + str(b) + str(c) + "." + str(d) 

     
# define event handlers for buttons "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    global count2, count1, d, running
    timer.stop()
    if running == True:    
        count2 +=1
        if d == 0:
            count1 += 1
        running = False    

def reset():
    global t, count1, count2
    timer.stop()
    t = 0
    count1 = 0
    count2 = 0
    

# define event handler for timer with 0.1 sec interval
def tick ():
    global t 
    t += 1
     

# define draw handler
def draw (canvas):
    global count2, count1
    text = format(t)
    canvas.draw_text (text,(150,200),44, "Red" )
    canvas.draw_text (str(count1) + "/" + str(count2),(320, 60), 40, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 400)
                      

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
start_button = frame.add_button('Start', start,100)
stop_button = frame.add_button ("Stop", stop,100)
reset_button = frame.add_button ("Reset", reset,100)

# start frame
frame.start()
