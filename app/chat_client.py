#Alexander Hoppe
#alexander.hoppe@students.olin.edu
#1/27/16


import CN_Sockets# CN_Sockets adds ability to interrupt "while True" loop with ctl-C
from HW_1 import * #my encode and decode methods
import RC4_Demo
import RSA_Hoppe as RSA



class UDP_echoclient(object):
    """ Computer Networks Lab 4: Introduction to Sockets.  UDP Transmit example.
This code only transmits a udp message to a known IP_address ("127.0.0.1") and port_number (5280)
The UDP_RX module recieves and prints messages it is sent.
In this example, the UDP_TX process is the client, because the port number of the server (5280) is known to it.
The server, runing UDP_RX, determines the client's port number from each message it receives.

--ALEX
Now receives echoed messages and prints them, with RC4 encryption in between!

--2/3--
Now prompts server for RSA public key, then sends RC4 password, waits for confirmation, then starts the echo client.


"""


    def __init__(self,IP="127.0.0.1",Server_Address=("127.0.0.1",5280)):   # create a socket instance.
                                                            # the "address" is IPv4 address ("127.0.0.1") and port number (5280)
                                                            # "127.0.0.1" is a special IPv4 address indicating that the socket will be communicating
                                                            # over a simulated layer 1 and 2 within a single machine (Laptop or Pi)

        socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout
        # socket = CN_sockets.socket, which is socket.socket with a slignt modification to allow you to use ctl-c to terminate a test safely
        # CN_sockets.AF_INET is the constant 2, indicating that the address is in IPv4 format
        # CN_sockets.SOCK_DGRAM is the constant 2, indicating that the programmer intends to use the Universal Datagram Protocol of the Transport Layer

        with socket(AF_INET,SOCK_DGRAM) as sock:  # open the socket

            # Prompt server to connect
            print ('starting connection')
            sock.sendto(UTF8_encode('<con>'), Server_Address)
            #wait for connected prompt
            sock.recv(1024)
            print('connected')
            #Send RSA public key
            rsa = RSA.RSA(message_bit_length=16)
            sock.sendto(UTF8_encode('<key>'+rsa.public.export_public_key()), Server_Address)
            print('key sent')
            #wait for RC4 pword
            encrypted_pword = UTF8_decode(sock.recv(1024))
            """
            THIS IS WHERE IT BREAKS

            I can't get the decryption to work, and it's 3 AM.
            """

            clear_pword = rsa.private.decrypt(int(encrypted_pword))
            rc4 = RC4_Demo.Olin_RC4(bytes(clear_pword))
            print('RC4 password received')


            print ("UDP_TX client started for UDP_Server at IP address {} on port {}".format(Server_Address[0],Server_Address[1]))


            # Echo loop
            while True:
                #message sending
                str_message = input("Enter message to send to server:\n")

                if not str_message: # an return with no characters terminates the loop
                    break

                #encode bytes
                bytearray_cleartext = UTF8_encode(str_message)

                #cipher bytes
                bytearray_cipher = rc4.crypt(bytearray_cleartext)

                bytes_sent = sock.sendto(bytearray_cipher, Server_Address) # this is the command to send the bytes in bytearray to the server at "Server_Address"

                print ("{} bytes sent".format(bytes_sent)) #sock_sendto returns number of bytes send.

                try:
                    #receiving scan
                    bytearray_encrypted, source_address = sock.recvfrom(1024) # 1024 is the buffer length
                                                                 # allocated for receiving the
                                                                 # datagram (i.e., the packet)

                    source_IP, source_port = source_address    # the source iaddress is ("127.0.0.1",client port number)
                                                               # where client port number is allocated to the TX process
                                                               # by the Linux kernel as part of the TX network stack))

                    print ("\nMessage received from ip address {}, port {}:".format(
                        source_IP,source_port))

                    bytearray_msg = rc4.crypt(bytearray_encrypted)

                    print (UTF8_decode(bytearray_msg))

                except timeout:
                    #it didn't get echoed back in time
                    print('Message failed')

                    continue #wait again

        print ("UDP_Client ended")




if __name__ == "__main__":
    UDP_echoclient()
