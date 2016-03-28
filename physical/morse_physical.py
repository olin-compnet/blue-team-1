
## Lab 2.2 - Physical Layer  - Send Tuples as blinks
#
from MorseTX import MorseTX
from SetPin import SetPin
import time

DIT_DUR = 0.001

#
#SENDING MORSE
#

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

#
#RECEIVING MORSE
#

symbol_q = Queue(100)

DIT_DUR = 0.001 # seconds

SAMPLES_PER_DIT = 10
THRESHOLD = SAMPLES_PER_DIT / 2
SAMPLE_PERIOD = DIT_DUR / SAMPLES_PER_DIT
SAMPLE_FREQUENCY = 1 / SAMPLE_PERIOD

DIT_SCALE    = 1
DAH_SCALE    = 3
EL_SCALE     = 1
LETTER_SCALE = 3
WORD_SCALE   = 7
EOM_SCALE    = 10

DIT_MIN_DUR  = DIT_DUR * (DIT_SCALE    + 0            ) * 0.5
DIT_MAX_DUR  = DIT_DUR * (DIT_SCALE    + DAH_SCALE    ) * 0.5

EL_MIN_DUR   = DIT_DUR * (EL_SCALE     + 0            ) * 0.5 # Threshold to see Element separator (lower end)
EL_MAX_DUR   = DIT_DUR * (EL_SCALE     + LETTER_SCALE ) * 0.5 # Threshold to see
CHAR_MAX_DUR = DIT_DUR * (LETTER_SCALE + WORD_SCALE   ) * 0.5
WORD_MAX_DUR = DIT_DUR * (WORD_SCALE   + EOM_SCALE    ) * 0.5

SYMBOLS_2_CHAR = {
    ".-"   : 'A', "-..." : 'B', "-.-." : 'C',
    "-.."  : 'D', "."    : 'E', "..-." : 'F',
    "--."  : 'G', "...." : 'H', ".."   : 'I',
    ".---" : 'J', "-.-"  : 'K', ".-.." : 'L',
    "--"   : 'M', "-."   : 'N', "---"  : 'O',
    ".--." : 'P', "--.-" : 'Q', ".-."  : 'R',
    "..."  : 'S', "-"    : 'T', "..-"  : 'U',
    "...-" : 'V', ".--"  : 'W', "-..-" : 'X',
    "-.--" : 'Y', "--.." : 'Z'# , "-----": '0',
    # ".----": '1', "..---": '2', "...--": '3',
    # "....-": '4', ".....": '5', "-....": '6',
    # "--...": '7', "---..": '8', "----.": '9'
}

DIT = '.'
DAH = '-'
CHAR_SEPARATOR = '#'
WORD_SEPARATOR = ' '
EOM = '\n'

def read_pin(RXpin):
    return 1 if RXpin.read_pin() else 0
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
