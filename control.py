#control and listen to the clicks of the mouse
#control and listen to the keyboard
#mouse and keyboard cant be controlled together

#from pynput.mouse import Controller  #here, we need to CONTROL the MOUSE.
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (500,820) #(10,20) is (left to right,top to bottom)

#controlMouse()
def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hey this is me!!")
    
controlKeyboard()
