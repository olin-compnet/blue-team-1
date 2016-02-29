#Alexander Hoppe
#alexander.hoppe@students.olin.edu
#1/27/16


import CN_Sockets
import RC4_Demo
from HW_1 import * #my encode and decode methods
import random
import RSA_Hoppe as RSA

class UDP_echoserver(object):
    """1. READ the UDP_TX module before reading or using this one.

This module demonstrates receiving a transmission sent by the UDP_TX module
on a SOCK_DGRAM (UDP) socket.  This module must be started first, so that it
can publish its port address (5280).

2. Run this module before starting UDP_TX.

UDP_TX and UDP_RX will be started on separate (laptop OS) processes.
UDP_TX will prompt for a message, then transmit it to the UDP_RX module over the
loopback IP address ("127.0.0.1").

UDP_RX will receive the message and print it.
While waiting for a message UDP_RX to be started or to send another message, UDP_TX will print a line of "."s one every 2 seonds.

--ALEX
Now echoes messages back to UDP client, with RC4 encryption in between!

2/3
Made an IRC client. Whoop.

    """


    def __init__(self,IP="127.0.0.1",port=5280):

        socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout
        #                                      the socket class    the IPv4 address model    The UDP layer 4 protocol    The event name for a socket timout

        #holds onto all the connected clients, in source address and RC4 pairs.
        clients = {}

        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.bind((IP,port))  # bind socket to port number

            sock.settimeout(2.0) # create a 2 second timeout so that we
                                 # can use ctrl-c to stop a blocked server
                                 # if, for example, the client doesn't work.

            print ("UDP Server started on IP Address {}, port {}".format(IP,port))
            #scan for input
            while True:
                #repeat the echo scan
                try:
                    bytearray_received, source_address = sock.recvfrom(1024) # 1024 is the buffer length
                                                                 # allocated for receiving the
                                                                 # datagram (i.e., the packet)

                    source_IP, source_port = source_address    # the source iaddress is ("127.0.0.1",client port number)
                                                               # where client port number is allocated to the TX process
                                                               # by the Linux kernel as part of the TX network stack))
                    msg = ''
                    #decode if in RC4, else leave clear
                    if source_address in clients.keys():
                        decrypted = clients[source_address].crypt(bytearray_received)
                        msg = UTF8_decode(decrypted)
                    else:
                        msg = UTF8_decode(bytearray_received)

                    #trying to connect
                    if msg == '<con>':
                        sock.sendto(UTF8_encode('<con>'), source_address)
                        print('client connected')
                        continue

                    #RSA RC4 exchange
                    if msg[:5] == '<key>':
                        #get public key
                        print('init RSA/RC4 exchange')
                        #make an empty RSA_public to import into
                        public = RSA.RSA_Public(1, 1)
                        public.import_public_key(msg[5:])

                        print(str(public.n) + '|'+ str(public.e))

                        #generate an RC4 password
                        pword = random.randrange(1,9998)
                        print(pword)
                        #add it to clients dict
                        clients[source_address] = RC4_Demo.Olin_RC4(bytes(pword)) #something's messed up with types here.
                        print(clients)
                        #send it over!
                        cipherpword = public.encrypt(pword, (public.n, public.e))
                        print(cipherpword)
                        sock.sendto(UTF8_encode(str(cipherpword)), source_address)
                        print('RC4 pword encrypted and sent')
                        continue

                    #Begin sending to all clients.
                    print(str(source_address) + ':\n' + msg)
                    #say who it's from
                    msg = str(source_address) + ' >> ' + msg

                    #send it to everyone.
                    for key in clients:
                        #encrypt according to the right rc4 for the client
                        encrypted = clients[key].crypt(UTF8_encode(msg))

                        #send to client
                        sock.sendto(encrypted, key)


                except timeout:

                    print (".",end="",flush=True)  # if process times out, just print a "dot" and continue waiting.  The effect is to have the server print  a line of dots
                                                   # so that you can see if it's still working.
                    continue  # go wait again

if __name__ == "__main__":
    UDP_echoserver()
