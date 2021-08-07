import pyautogui as pt
from time import sleep

while True:
    posXY = pt.position() # position of the mouse pointer
    print(posXY, pt.pixel(posXY[0],posXY[1]))
    sleep(1) # delay a little bit

    #stop condition:
    if posXY[0] == 0:
        break