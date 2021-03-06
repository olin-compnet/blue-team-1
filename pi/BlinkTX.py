#
## Lab 2.2 - Physical Layer  - Send Tuples as blinks
#
from MorseTX import MorseTX
from SetPin import SetPin
import time

DIT_DUR = 0.1

class BlinkTX(SetPin):
    def __init__(self,headerpin,BCM,direction="TX"):
        if direction != "TX":
            raise ValueError("direction must be 'TX'")
        super().__init__(headerpin,BCM,direction="TX")
    def __call__(self,tups):
        for state,direction in tups:
            self.blinkTX(state,direction)
    def blinkTX(self,state,duration):
        self.turn_high() if state else self.turn_low()
        time.sleep(duration * DIT_DUR)

def send_morse(msg):
    with BlinkTX(15,"GPIO_22",direction="TX") as blink:
        blink(MorseTX(msg.upper()))

if __name__ == "__main__":
    import random
    import mobydickquotes
    import string
    import unicodedata
    quotes = mobydickquotes.quotes

    def getquote():
        return makeMorseHappy(quotes[random.randint(0,len(quotes)-1)])

    def makeMorseHappy(Q):
        return "".join([a if a in string.ascii_uppercase+" " else " "+"".join(unicodedata.name(a,"").split("-"))+" " for a in Q.upper() ])

    with BlinkTX(15,"GPIO_22",direction="TX") as blink:
        while True:
            msg = input("MESSAGE TO SEND (EMPTY ENTRY YIELDS RANDOM QUOTE) :")
            if not msg:
                blink(MorseTX(getquote()))
            elif msg.upper() == "QUIT":
                break
            else:
                blink(MorseTX(msg.upper()))
