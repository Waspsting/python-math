import sys
import os
import math
import time 


def xy_print(text, x=0, y=0):
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.write("\033[K")
    sys.stdout.write(text)
    sys.stdout.flush()

def fix_right():
    pass #TODO!!! 
    
term_width = os.get_terminal_size().columns
term_height = os.get_terminal_size().lines
# main code type script
top_text = "┌" + ("─" * (term_width-2)) + "┐"
mid_text = "│" + (" " * (term_width-2)) + "│"
bot_text = "└" + ("─" * (term_width-2)) + "┘"

xy_print(top_text,x=0,y=0)

for i in range(term_height-2):
    xy_print(mid_text,x=0,y=i+2)

xy_print(bot_text,x=0,y=term_height)

for i in range(term_width-2):
    fn_x = i + 2
    fn_y = (term_height-1) - ((10*(math.sin(0.25*fn_x)))+15)
    time.sleep(0.1)
    xy_print(".",x=math.floor(fn_x), y=math.floor(fn_y))

while True:
    pass
