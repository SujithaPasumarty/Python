# template for "Stopwatch: The Game"
import simplegui
# define global variables

time=0
minutes=0
seconds=0
tseconds=0
total_stops=0
successful_stops=0
flag="true"
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
            global minutes,seconds,tseconds
            minutes=int((time/(10*60))%60)
            seconds=int((time/10)%60)
            tseconds=int(time%10)
            return "%d:%02d.%02d"%(minutes,seconds,tseconds)
        
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global flag
    flag="true"
    t.start()
    
def stop():
    global minutes,seconds,tseconds,successful_stops,total_stops,flag
    if(flag=="true"):
        t.stop()
        if(tseconds==0):
            successful_stops=successful_stops+1
            total_stops=total_stops+1
            flag="false"
        elif(tseconds>0):
            total_stops=total_stops+1
            flag="false"
    else:
        total_stops=total_stops
def reset():
    global time,successful_stops,total_stops
    time=0
    successful_stops=0
    total_stops=0
    format()
    t.stop()
# define event handler for timer with 0.1 sec interval
def tick():
     global time
     time=time+1
     format()
# define draw handler
def draw(canvas):
    global tseconds,seconds,minutes,counter,total_chances
    s=str(successful_stops)+"/"+str(total_stops)
    canvas.draw_text(format(),(50,100),40,"White")
    canvas.draw_text(s,(150,30),20,"Green")
    
# create frame
f=simplegui.create_frame("Stop Watch",200,200)
t=simplegui.create_timer(100,tick)

# register event handlers
f.add_button("Start",start,100)
f.add_button("Stop",stop,100)
f.add_button("Reset",reset,100)
f.set_draw_handler(draw)

# start frame
f.start()



