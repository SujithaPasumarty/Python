# Implementation of classic arcade game Pong
import simplegui
import random
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
ball_pos=[WIDTH/2,HEIGHT/2]
direction=True
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(dir):
    global ball_pos, ball_vel # these are vectors stored as lists
    if dir==True:
        ball_vel=[random.randrange(2,5),-random.randrange(1,4)]
    else:
        ball_vel = [-random.randrange(2, 5),-random.randrange(1, 4)]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,direction  # these are numbers
    global score1, score2  # these are ints
    score1=0
    score2=0
    paddle1_vel=0
    paddle2_vel=0
    paddle1_pos=(HEIGHT-PAD_HEIGHT)/2
    paddle2_pos=(HEIGHT-PAD_HEIGHT)/2
    spawn_ball(direction)
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,BALL_RADIUS
    global paddle1_vel,paddle2_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[0]<=BALL_RADIUS+ PAD_WIDTH:
        if paddle1_pos <=ball_pos[1]<=(paddle1_pos+PAD_HEIGHT):
            ball_vel[0]=-1.1*ball_vel[0]
        else:
            spawn_ball(True)
            score2+= 1
    elif ball_pos[0]>=(WIDTH-BALL_RADIUS-PAD_WIDTH):
        if paddle2_pos<= ball_pos[1]<=(paddle2_pos+PAD_HEIGHT):
            ball_vel[0]= -1.1*ball_vel[0]
        else:
            spawn_ball(False)
            score1+=1
    if ball_pos[1]<=BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    elif ball_pos[1]>=(HEIGHT-BALL_RADIUS):
        ball_vel[1]=-ball_vel[1]
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"White","White")
   
    # draw paddles
    canvas.draw_line([(PAD_WIDTH/2),paddle1_pos],[(PAD_WIDTH/2),(paddle1_pos+PAD_HEIGHT)],PAD_WIDTH,"WHITE")
    canvas.draw_line([(WIDTH-(PAD_WIDTH/2)),paddle2_pos],[(WIDTH-(PAD_WIDTH/2)),(paddle2_pos+PAD_HEIGHT)],PAD_WIDTH,"WHITE")
     # update paddle's vertical position, keep paddle on the screen
    if 0<=(paddle1_pos+paddle1_vel)<=HEIGHT-PAD_HEIGHT:
        paddle1_pos+=paddle1_vel
    if 0<=(paddle2_pos + paddle2_vel)<=HEIGHT-PAD_HEIGHT:
        paddle2_pos+=paddle2_vel 

    # draw scores
    canvas.draw_text(str(score1),(150,40),40,"White")
    canvas.draw_text(str(score2),(450,40),40,"White")    
def keydown(key):
    global paddle1_vel, paddle2_vel
    velocity_paddle=3
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel=velocity_paddle
    if key==simplegui.KEY_MAP["up"]:
        paddle1_vel=-velocity_paddle
    if key==simplegui.KEY_MAP["w"]:
        paddle2_vel=-velocity_paddle
    if key==simplegui.KEY_MAP["s"]:
        paddle2_vel=velocity_paddle   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel=0
    if key==simplegui.KEY_MAP["up"]:
        paddle1_vel=0
    if key==simplegui.KEY_MAP["w"]:
        paddle2_vel=0
    if key==simplegui.KEY_MAP["s"]:
        paddle2_vel=0    
def button_handler():
    new_game()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",button_handler,100)
# start frame
new_game()
frame.start()
