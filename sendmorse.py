#SENDING MORSE CODE

from  SetPin import SetPin
from MorseCode import MorseCode as mc
import time

# Base unit
DIT_DUR = 1 #seconds


DAH_DUR = 3 * DIT_DUR

LETTER_DUR = 3 * DIT_DUR # Time between letters
WORD_DUR = 7 * DIT_DUR # Time between letters

VALID_CHARS = ['']

	def send_string(string):

        for c in string:
            send_char(c)


    def send_char(char):
        pass

    def send_dah():
        TXpin.turn_high()
        time.sleep(DIT_DUR)
        TXpin.turn_low()

    def send_dit():
        TXpin.turn_high()


if __name__ == "__main__":
    with SetPin(15, "GPIO_22", direction="TX") as TXpin:
        send_string("HELLO WORLD")
