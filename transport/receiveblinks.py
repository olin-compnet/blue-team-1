#
## Introducton to Python breadboarding - Receive Blinks
#
from  SetPin import SetPin
import time

def receiveblinks(RXpin,blinks=200,duration=.25):
    for i in range(blinks):
        print("|{}".format("==" if RXpin.read_pin() else ""))

if __name__ == "__main__":   
            
    with SetPin(16,"GPIO_23",direction="RX") as RXpin:
    	while True:
        	receiveblinks(RXpin)
