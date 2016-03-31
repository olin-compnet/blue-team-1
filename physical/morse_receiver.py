################
# Receive code #
################

from SetPin import SetPin
import time
import threading
from queue import Queue

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
DIT_MAX_DUR  = DIT_DUR * (DIT_SCALE    + DAH_SCALE    ) * 0.5 #Ask Mitchell

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

# yields True if high unit, else False
# def read_unit():
#     '''
#     Continuously generates a unit read over one DIT_DUR.  Ideally, this oversamples
#     If the total_high_count exceeds the THRESHOLD, then returns True meaning that it is determined to be a HIGH or a '1'
#     Otherwise False, LOW, or '0'
#     '''
#     drift = 0
#     last_was_high = False
#     while True:
#         total_high_count = 0 if last_was_high else drift
#         drift = 0

#         for i in range(SAMPLES_PER_DIT - drift):
#             read = read_pin()
#             total_high_count = total_high_count + read # Assume 1 if true else 0

#             # For each unexpected read, increase the drift by 1
#             if 1 ^ read ^ last_was_high:
#                 if i > SAMPLES_PER_DIT / 2:
#                     drift = drift + 1
#                 else:
#                     drift = drift -1
#             time.sleep(SAMPLE_PERIOD)

#         last_was_high = total_high_count > THRESHOLD
#         yield last_was_high


# # Yield dit, dah, element_sep, word_sep, EOM
# def read_symbol():
#     '''
#     Collects units of inputs from read_unit such as: 1 0 111 0 1 000 111 0 1 0 1 0000000 1 and converts it to:
#     DIT, DAH, DIT, CHAR_SEPARATOR, DAH, DIT, DIT, WORD_SEPARATOR, DIT
#     Each time this generator is called, yields one symbol
#     ENDS when consecutive 0s meet or exceeds EOM_SCALE.  yields EOM when this happens
#     '''
#     state_is_high = True
#     consecutive_read = 1
#     for unit in read_unit():
#         if unit == state_is_high:
#             consecutive_read = consecutive_read + 1
#             if consecutive_read >= EOM_SCALE and not state_is_high:
#                 yield EOM
#                 break
#         else:
#             if state_is_high:
#                 if consecutive_read < DAH_SCALE: # Counts of
#                     yield DIT
#                 else:
#                     yield DAH
#             else:
#                 # Smaller than LETTER_SCALE Therefore element separator
#                 if consecutive_read < LETTER_SCALE:
#                     pass
#                 # Smaller than WORD_SCALE, therefore letter separator
#                 elif consecutive_read < WORD_SCALE:
#                     yield CHAR_SEPARATOR
#                 # Smaller than EOM_SCALE, therefore word separator
#                 elif consecutive_read < EOM_SCALE:
#                     yield WORD_SEPARATOR
#                 # As big as EOM_SCALE or bigger, probably means we're done with this message
#                 else:
#                     yield EOM
#                     break

#             # Flip state
#             state_is_high = not state_is_high
#             consecutive_read = 1

# Version 2 of read_symbol
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


# def read_symbol_test():
#     temp_fn = read_unit
#     # Hardcoded output for a unit reading of '.-#-.. .E'
#     def read_unit():
#         return [
#             True, False,                # DIT
#             True, True, True,           # DAH
#             False, False, False,        # CHAR_SEPARATOR
#             True, True, True, False,    # DAH
#             True, False,                # DIT
#             True, False,                # DIT
#             False, False, False, False, False, False, # WORD_SEPARATOR
#             True,                       # DIT
#             False, False, False, False, False, False, False, False, False, False, False, False] # EOM

#     string = ''.join([symbol for symbol in read_symbol])
#     expected = DIT + DAH + CHAR_SEPARATOR + DAH + DIT + DIT + WORD_SEPARATOR + DIT
#     if string != expected:
#         read_unit = temp_fn
#         raise Exception("Test case not passed, expected '.-#-. .', got " + string)

#     read_unit = temp_fn
#     temp_fn = None


# def read_chars():
#     '''
#     Collects symbols and generates characters from these symbols.
#     Yields a single character at a time from the string.
#     ENDS when EOM is detected by read_symbol
#     '''
#     symbols = ''
#     for symbol in read_symbol():
#         # Collect symbols
#         if symbol is DIT or symbol is DAH:
#             symbols = symbols + symbol

#         # yield character when end of symbol
#         elif symbol is CHAR_SEPARATOR:
#             if symbols in SYMBOLS_2_CHAR:
#                 yield SYMBOLS_2_CHAR[symbols]
#             else:
#                 raise ValueError('symbol pattern not recognize: ' + symbols)
#             symbols = ''

#         # Next word
#         elif symbol is WORD_SEPARATOR:
#             yield ' '

#         # End of message
#         elif symbol is EOM:
#             break
#         else:
#             raise ValueError('unrecognized symbol: ' + symbol)

# def read_chars_test():
#     temp_fn = read_symbol
#     # Expected output: ABC DEF GHI
#     def read_symbol():
#         return
#         [
#             DIT, DAH,           CHAR_SEPARATOR, # A
#             DAH, DIT, DIT, DIT, CHAR_SEPARATOR, # B
#             DAH, DIT, DAH, DIT, CHAR_SEPARATOR, # C
#                                 WORD_SEPARATOR,
#             DAH, DIT, DIT,      CHAR_SEPARATOR, # D
#             DIT,                CHAR_SEPARATOR, # E
#             DIT, DIT, DAH, DIT, CHAR_SEPARATOR, # F
#                                 WORD_SEPARATOR,
#             DAH, DAH, DIT,      CHAR_SEPARATOR, # G
#             DIT, DIT, DIT, DIT, CHAR_SEPARATOR, # H
#             DIT, DIT,           CHAR_SEPARATOR, # I
#                                 EOM
#         ]

#     string = ''
#     for char in read_chars():
#         string = string + char
#     if string != "ABC DEF GHI":
#         raise Exception('read_char failed, expected "ABC DEF GHI", got ' + string)
#     read_symbol = temp_fn

# Version 2 of read_chars.  Obtains from symbol_q in a blocking fashion
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
            # print("DONE")


    # while True:
    #     idle()
    #     #parse first symbol
    #     for char in read_chars():
    #         print(char, end='')
    #     print()


if __name__ == "__main__":
    for msg in receive_morse():
        print(msg)
