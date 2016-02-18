#
## Introducton to Python breadboarding - Receive Blinks
#
from  SetPin import SetPin
import time
import sys

def receiveblinks(RXpin,blinks=200,duration=.01):
    for i in range(blinks):
        time.sleep(duration)
        print("{}".format("|" if RXpin.read_pin() else "."),end="\n")
        sys.stdout.flush()

if __name__ == "__main__":   
            
    with SetPin(16,"GPIO_23",direction="RX") as RXpin:
        while True:
            receiveblinks(RXpin)
