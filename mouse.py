from pynput.mouse import Listener

def writetofile(x,y):
    print("the postion is {0}".format((x,y)))

with Listener(on_move=writetofile) as M:
    M.join()