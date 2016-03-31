
## Lab 2.2 - Physical Layer  - Send Tuples as blinks
#
from MorseTX import MorseTX
from SetPin import SetPin
import time
from queue import Queue

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

def read_symbol(RXpin):
    idle()
    last_time = time.time()
    while True:
        state_is_high = read_pin(RXpin)
        while state_is_high == read_pin(RXpin) and time.time() - last_time < DIT_DUR * EOM_SCALE:
            time.sleep(SAMPLE_PERIOD) # Artifically slowing down reads so that we don't do a bajillion comparisons w/o reason

        end_time = time.time()
        delta_time = end_time - last_time

        if state_is_high:
            if delta_time < DIT_MIN_DUR:
                print("Very small positive blip found, ignoring")
                end_time = last_time
            elif delta_time < DIT_MAX_DUR:
                symbol_q.put(DIT)
                # yield DIT
            else:
                symbol_q.put(DAH)
                # yield DAH
        else:
            if delta_time < EL_MIN_DUR:
                print("Very small negative blip found, ignoring")
                end_time = last_time
            elif delta_time < EL_MAX_DUR:
                pass
            elif delta_time < CHAR_MAX_DUR:
                symbol_q.put(CHAR_SEPARATOR)
                # yield CHAR_SEPARATOR
            elif delta_time < WORD_MAX_DUR:
                symbol_q.put(WORD_SEPARATOR)
                # yield WORD_SEPARATOR
            else:
                symbol_q.put(EOM)
                # yield EOM
                break
        last_time = end_time

def read_chars():
    symbols = ""
    symbol = symbol_q.get()
    while symbol:
        if symbol == DIT or symbol == DAH:
            symbols = symbols + symbol

        else:
            if symbols in SYMBOLS_2_CHAR:
                yield SYMBOLS_2_CHAR[symbols]
            else:
                yield symbols

            if symbol == CHAR_SEPARATOR:
                pass

            elif symbol == WORD_SEPARATOR:
                yield " "
            elif symbol == EOM:
                return '\n'

            symbols = "" # Reset symbols

        symbol = symbol_q.get()

def process():
    for char in read_chars():
        print(char, end="", flush=True)
    print("\n")

def idle():
    '''
    Does nothing until the pin reads something positive
    '''
    while not read_pin(RXpin):
        pass

def receive_morse():
    # End Of Message: .-.-. ***deprecated
    """
    demo receiving

    for i in range(blinks):
            print("|{}".format("==" if  RXpin.read_pin() else ""))
    """
    global RXpin
    with SetPin(16,"GPIO_23",direction="RX") as RXpin:
        #wait for signal
        while True:
            read_symbol_thread = threading.Thread(target=read_symbol, name="SymbolMaker", args=(RXpin,))
            read_char_thread = threading.Thread(target=process, name="SymbolProcessor")
            read_symbol_thread.start()
            read_char_thread.start()
            read_symbol_thread.join()
            read_char_thread.join()

if __name__ == "__main__":
    import random
    import mobydickquotes
    import string
    import unicodedata
    import threading
    quotes = mobydickquotes.quotes

    def getquote():
        return makeMorseHappy(quotes[random.randint(0,len(quotes)-1)])

    def makeMorseHappy(Q):
        return "".join([a if a in string.ascii_uppercase+" " else " "+"".join(unicodedata.name(a,"").split("-"))+" " for a in Q.upper() ])

    def send():
        with BlinkTX(15,"GPIO_22",direction="TX") as blink:
            while True:
                msg = input("MESSAGE TO SEND (EMPTY ENTRY YIELDS RANDOM QUOTE) :")
                if not msg:
                    blink(MorseTX(getquote()))
                elif msg.upper() == "QUIT":
                    break
                else:
                    blink(MorseTX(msg.upper()))
    def receive():
        for msg in receive_morse():
            print(msg)

    receive_thread = threading.Thread(target=receive, name='RECEIVER')
    send_thread = threading.Thread(target=send, name='SENDER')
    try:
        receive_thread.start()
        send_thread.start()
    except(KeyboardInterrupt, SystemExit):
        cleanup_stop_thread();
        sys.exit()
    receive_thread.join()
    send_thread.join()
