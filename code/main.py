import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

# locate smiley face on screen:
startPosition = pt.locateOnScreen("images/smile_paperclip.png", confidence=.60) 
# obs.: using confidence because, if we don't, a slight variation in the image will cause failure
# in our localization.

x = startPosition[0]
y = startPosition[1]

# Gets message received in whatsapp chat.
def get_message():
    global x, y

    position = pt.locateOnScreen("images/smile_paperclip.png", confidence=.60) 
    x = position[0]
    y = position[1]

    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x+90,y-50, duration=.5) # mouse is on top of last message.
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20,-195)
    pt.click()
    whatsappMessage = pyperclip.paste()
    #pt.click()
    #print("Message received:", whatsappMessage)

    return whatsappMessage

# Posts
def post_response(message):
    global x,y

    position = pt.locateOnScreen("images/smile_paperclip.png", confidence=.60) 
    x = position[0]
    y = position[1]

    pt.moveTo(x+200, y+20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01) # 100 words per second.
    pt.typewrite("\n", interval=.01) # enter to send message.

def process_response(message):
    #randomNumber = random.randrange(3)
    return "Testando chatbot!"

# Checks for new messages:
def checks_for_new_messages():
    #global x,y
    #pt.moveTo(x+90, y-35)

    while True:
        #Continuously check for green dot and new messages
        try:
            position = pt.locateOnScreen("images/green_circle.png", confidence=.8)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(1)
        except(Exception):
            print("No new messages located from any other users.")

        # if color to which the mouse points is white:
        if pt.pixelMatchesColor(int(x+90), int(y-35), (255,255,255), tolerance=10):
            #print("is_white")
            processed_response = process_response(get_message())
            post_response(processed_response)
        else:
            print("No new messages yet...")
        sleep(5)

checks_for_new_messages()

