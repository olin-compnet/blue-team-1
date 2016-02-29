################
# Receive code #
################

from SetPin import SetPin
import time

DIT_DUR = 0.1 # seconds

SAMPLES_PER_DIT = 4
THRESHOLD = SAMPLES_PER_DIT * 3 / 4.0
SAMPLE_PERIOD = DIT_DUR / SAMPLES_PER_DIT
SAMPLE_FREQUENCY = 1 / SAMPLE_PERIOD

DIT_SCALE    = 1
DAH_SCALE    = 3
EL_SCALE     = 1
LETTER_SCALE = 3
WORD_SCALE   = 7
EOF_SCALE    = 10
SYMBOLS_2_CHAR = {
    ".-"   : 'A', "-..." : 'B', "-.-." : 'C',
    "-.."  : 'D', "."    : 'E', "..-." : 'F',
    "--."  : 'G', "...." : 'H', ".."   : 'I',
    ".---" : 'J', "-.-"  : 'K', ".-.." : 'L',
    "--"   : 'M', "-."   : 'N', "---"  : 'O',
    ".--." : 'P', "--.-" : 'Q', ".-."  : 'R',
    "..."  : 'S', "-"    : 'T', "..-"  : 'U',
    "...-" : 'V', ".--"  : 'W', "-..-" : 'X',
    "-.--" : 'Y', "--.." : 'Z', "-----": '0',
    ".----": '1', "..---": '2', "...--": '3',
    "....-": '4', ".....": '5', "-....": '6',
    "--...": '7', "---..": '8', "----.": '9'
}

DIT = '.'
DAH = '-'
CHAR_SEPARATOR = '#'
WORD_SEPARATOR = ' '
EOM = '\n'

def read_pin():
    return 1 if RXpin.read_pin() else 0

# yields True if high unit, else False
def read_unit():
    while True:
        total_high_count = 0

        for i in range(SAMPLES_PER_DIT):
            total_high_count = total_high_count + read_pin() # Assume 1 if true else 0
            time.sleep(SAMPLE_PERIOD)

        yield total_high_count > THRESHOLD

# Yield dit, dah, element_sep, word_sep, EOM
def read_symbol():
    state_is_high = True
    consecutive_read = 1
    for unit in read_unit():
        if unit == state_is_high:
            consecutive_read = consecutive_read + 1
            if consecutive_read >= EOF_SCALE and not state_is_high:
                yield EOM
                break
        else:
            if state_is_high:
                if consecutive_read < DAH_SCALE: # Counts of
                    yield DIT
                else:
                    yield DAH
            else:
                # Smaller than LETTER_SCALE Therefore element separator
                if consecutive_read < LETTER_SCALE:
                    pass
                # Smaller than WORD_SCALE, therefore letter separator
                elif consecutive_read < WORD_SCALE:
                    yield CHAR_SEPARATOR
                # Smaller than EOF_SCALE, therefore word separator
                elif consecutive_read < EOF_SCALE:
                    yield WORD_SEPARATOR

                # As big as EOF_SCALE or bigger, probably means we're done with this message
                else:
                    yield EOM
                    break

            state_is_high = not state_is_high
            consecutive_read = 1

def read_symbol_test():
    temp_fn = read_unit
    # Hardcoded output for a unit reading of '.-#-.. .E'
    def read_unit():
        return [
            True, False,                # DIT
            True, True, True,           # DAH
            False, False, False,        # CHAR_SEPARATOR
            True, True, True, False,    # DAH
            True, False,                # DIT
            True, False,                # DIT
            False, False, False, False, False, False, # WORD_SEPARATOR
            True,                       # DIT
            False, False, False, False, False, False, False, False, False, False, False, False] # EOM

    string = ''.join([symbol for symbol in read_symbol])
    expected = DIT + DAH + CHAR_SEPARATOR + DAH + DIT + DIT + WORD_SEPARATOR + DIT
    if string != expected:
        read_unit = temp_fn
        raise Exception("Test case not passed, expected '.-#-. .', got " + string)

    read_unit = temp_fn
    temp_fn = None

def read_chars():
    symbols = ''
    for symbol in read_symbol():

        # Collect symbols
        if symbol is DIT or symbol is DAH:
            symbols = symbols + symbol
        else:
            if symbols in SYMBOLS_2_CHAR:
                yield SYMBOLS_2_CHAR[symbols]
            else:
                raise ValueError('symbol pattern not recognize: ' + symbols)
            symbols = ''

            if symbol is CHAR_SEPARATOR:
                continue
            # Next word
            elif symbol is WORD_SEPARATOR:
                yield ' '

            # End of message
            elif symbol is EOM:
                break
            else:
                raise ValueError('unrecognized symbol: ' + symbol)

def read_chars_test():
    temp_fn = read_symbol
    # Expected output: ABC DEF GHI
    def read_symbol():
        return
        [
            DIT, DAH,           CHAR_SEPARATOR, # A
            DAH, DIT, DIT, DIT, CHAR_SEPARATOR, # B
            DAH, DIT, DAH, DIT, CHAR_SEPARATOR, # C
            WORD_SEPARATOR,
            DAH, DIT, DIT,      CHAR_SEPARATOR, # D
            DIT,                CHAR_SEPARATOR, # E
            DIT, DIT, DAH, DIT, CHAR_SEPARATOR, # F
            WORD_SEPARATOR,
            DAH, DAH, DIT,      CHAR_SEPARATOR, # G
            DIT, DIT, DIT, DIT, CHAR_SEPARATOR, # H
            DIT, DIT,           CHAR_SEPARATOR, # I
            EOM
        ]

    string = ''
    for char in read_chars():
        string = string + char
    if string != "ABC DEF GHI":
        raise Exception('read_char failed, expected "ABC DEF GHI", got ' + string)
    read_symbol = temp_fn


def idle():
    '''
    Does nothing until the pin reads something positive
    '''
    while not read_pin():
        pass

def receive_morse():
    # End Of Message: .-.-. ***deprecated
    """
    demo receiving

    for i in range(blinks):
            print("|{}".format("==" if  RXpin.read_pin() else ""))
    """
    #wait for signal
    global RXpin
    with SetPin(16,"GPIO_23",direction="RX") as RXpin:
        while True:
            idle()
            #parse first symbol
            yield ''.join([char for char in read_chars()])

if __name__ == "__main__":
    for msg in receive_morse():
        print(msg)
