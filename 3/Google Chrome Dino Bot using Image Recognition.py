from PIL import ImageGrab, ImageOps
from PIL import image
import pyautogui
import time
import numpy as np


class cordinates():
    # coordinates of replay button to start the game
    replaybutton = (360, 214)
    # this coordinates represent the top-right coordinates
    # that will be used to define the front box
    dinasaur = (149, 239)


def restartGame():
    # using pyautogui library, we are clicking on the
    # replay button without any user interaction
    pyautogui.click(cordinates.replaybutton)

    # we will keep our Bot always down that
    # will prevent him to get hit by bird
    pyautogui.keyDown('down')


def press_space():
    # releasing the Down Key
    pyautogui.keyUp('down')

    # pressing Space to overcome Bush
    pyautogui.keyDown('space')

    # so that Space Key will be recognized easily
    time.sleep(0.05)

    # printing the "Jump" statement on the
    # terminal to see the current output
    print("jump")
    time.sleep(0.10)

    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():

    box = (cordinates.dinasaur[0] + 30, cordinates.dinasaur[1],
           cordinates.dinasaur[0] + 120, cordinates.dinasaur[1] + 2)

    image = imageGrab.grab(box)

    # converting RGB to Grayscale to
    # make processing easy and result faster

    GreyImage = ImageOps.greyscale(image)

    a = np.array(greyImage.getcolors())

    print(a.sum())
    return a.sum()

restartGame()
while True:

     # 435 is the sum of white pixels values of box.
     # You may get different value is you are taking bigger

     if(imageGrab() != 435):
         press_space()

         time.sleep(0.1)
