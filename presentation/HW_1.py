#Alexander Hoppe
#alexander.hoppe@students.olin.edu
#1/26/16

def UTF8_encode(string):
    output = b''
    return output.join([UTF8_encode_helper(c) for c in string])


#helper function for encoding chars
def UTF8_encode_helper(char):
    code_point = ord(char)

    #initialize output for clarity
    b = []

    #figure out how many bytes we'll need
    cnbl = code_point.bit_length()
    byte_length = 1 + (cnbl > 7) + (cnbl > 11) + (cnbl > 16)

    if byte_length == 1:
        #just leave it as an int
        b = [code_point]
    elif byte_length == 2:
        #Combine the highest five bits of the code point and the header
        b1 = (code_point >> 6) | 0b11000000
        #Combine the rest of the code point and the second header
        b2 = (code_point & 0b00000111111) | 0b10000000
        #shift the first byte up 8 and combine it with the second byte
        b = [b1, b2]
    elif byte_length == 3:
        #Combine the highest four bits of the code point with the header
        b1 = (code_point >> 12) | 0b11100000
        #Combine the middle six bits of the code point with the second header
        b2 = ((code_point >> 6) & 0b0000111111) | 0b10000000
        #combine the lowest six bits of the code point with the second header
        b3 = (code_point & 0b0000000000111111) | 0b10000000
        #shift the bytes and combine them into one number
        b = [b1, b2, b3]
    else: #byte length is 4
        #Combine the highest three bits of the code point with the header
        b1 = (code_point >> 21) | 0b11110000
        #Combine the second highest six bits of the code point with the header
        b2 = ((code_point >> 12) & 0b000111111) | 0b10000000
        #Combine the third highest six bits of the code point with the header
        b3 = ((code_point >> 6) & 0b000000000111111) | 0b10000000
        #Combine the lowest six bits of the code point with the header
        b4 = (code_point & 0b000000000000000111111) | 0b10000000
        #Shift the bytes and combine them into one number
        b = [b1, b2, b3, b4]

    #return list of ints as bytes
    return bytes(b)

# THis doesn't work, but I tried for a long time. 
def UTF8_decode_bad(in_bytes):
    #turn bytes sequence into bytearray
    byte_array = bytearray(in_bytes)

    #initialize output accumulator
    output = ''

    #while there are still bytes coming in
    while len(byte_array) > 0:
        print(len(byte_array))
        #initialize code point accumulator
        code_string = ''

        #read in the first byte, convert to a binary string and trim off '0b'
        #Dhash told me to use strings for this.
        b1 = bin(byte_array.pop(0))[2:]
        #if the first bit is 0, its ASCII
        if b1[0] == '0':
            #set the output to the ASCII code point
            code_string = b1
        else: #have to figure out how long it is
            #count header bits
            byte_length = 0
            #convenient post-process increment works nicely with indices here
            while b1[byte_length] == '1':
                byte_length += 1

            #Slice code out of first byte (byte_length * '1' + '0' are useless )
            code_string += b1[byte_length + 2:]
            #iterate through rest of byte length, processing bytes
            for i in range(byte_length - 1):
                #read in byte, trim '0b10' header, add to code point string
                code_string += bin(byte_array.pop(0))[4:]

        #Decode the code point string into a character and add to output
        output += chr(int(code_string, 2))

    return output


def UTF8_decode(in_bytes):
    output = ''
    #turn bytes sequence into bytearray
    byte_array = bytearray(in_bytes)
    #keep running until we're out of bytes
    while len(byte_array):
        #check the first bit for ASCII
        b1 = byte_array.pop(0)
        if b1 < 128:
            output += chr(b1)
        else:
            #make sure this is in the right range
            assert(b1 > 191)
            #figure out how many bytes long it is via number range
            byte_length = 1 + (b1 > 191) + (b1 > 223) + (b1 > 239)
            #figure out code points
            c = []
            #Mask out code point in first bit
            c.append(b1 & (0b11111111 >> (byte_length + 1)))
            #Mask out the rest of the code points
            for i in range(byte_length-1):
                c.append(byte_array.pop(0) & 0b111111)
            #put the code points together, shifting them accordingly
            code_point = 0
            for i in range(len(c)):
                code_point = code_point | (c.pop() << (i*6))
            output += chr(code_point)

    return output

# Note: adapted from From rfc3629, page 4

#   cnbl < 8     0000 0000-0000 007F | 0xxxxxxx
#   cnbl > 7     0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#   cnbl > 11    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#   cnbl > 16    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
