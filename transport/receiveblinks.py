#
## Introducton to Python breadboarding - Receive Blinks
#
from  SetPin import SetPin
import time
import sys

def receiveblinks(RXpin,blinks=100,duration=(1/4)/10):
    for i in range(blinks):
        time.sleep(duration)
        print("{}".format("|" if RXpin.read_pin() else "."),end="")
        sys.stdout.flush()

if __name__ == "__main__":   
            
    with SetPin(16,"GPIO_23",direction="RX") as RXpin:
        while True:
            receiveblinks(RXpin)
            print("")
