# implementation of card game - Memory
import simplegui
import random
list1=[]
list2=[]
exposed=[]
state=0
canvas_height=100
canvas_width=800
num1=0
num2=0
turns=0
# helper function to initialize globals
def new_game():
    global list1, list2, exposed, state, num1, num2, turns  
    moves = 0  
    num = -1  
    num2 = -2  
    state = 0  
    turns=0
    exposed = [False]*16  
    list1 = range(8)  
    list2 = range(8)  
    list1.extend(list2) 
    random.shuffle(list1)      
# define event handlers
def mouseclick(pos):
    global turns, exposed, state, list1, num1, num2  
    num = pos[0] // (canvas_width/len(list1)) 
    if exposed[num] == False:  
        if state == 0:  
            exposed[num] = True  
            state = 1  
            num1 = num           
        elif state == 1:  
            exposed[num] = True  
            state = 2  
            num2 = num 
            turns=turns+1
        else: 
            state = 1  
            if list1[num1] != list1[num2]:  
                exposed[num1] = False  
                exposed[num2] = False  
            exposed[num] = True  
            num1 = num  
            num2 = -1        
    else:
        turns=turns                        
# draw handler   
def draw(canvas):
    x_pos = 0  
    x = 0  
    global turns,list1
    label.set_text("Turns =" + str(turns))  
    for number in list1:  
      global exposed  
      if exposed[x] == True:  
        canvas.draw_text(str(number), (x_pos, 50), 50, "white")  
          
      else:  
        canvas.draw_line((x_pos + 25, 0), (x_pos + 25, canvas_height), (canvas_width/len(list1)), "Green")  
      x+=1 
      x_pos += (canvas_width/len(list1))  
      canvas.draw_polyline([(x_pos, 0), (x_pos, canvas_height)], 2, "Red")
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", canvas_width, canvas_height)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
# get things rolling
new_game()
frame.start()
