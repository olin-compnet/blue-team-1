import CN_Sockets
from rsa import RSA
import RC4_Demo

class Bob_Server(object):
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


 
 

    """

    
    def __init__(self,IP="127.0.0.1",port=5280):

        socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout
        #                                      the socket class    the IPv4 address model    The UDP layer 4 protocol    The event name for a socket timout
        
        
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.bind((IP,port))  # bind sets up a relationship in the linux
                                  # kernel between the process running
                                  # UCP_RX and the port number (5280 by default)
                                  # 5280 is an arbitrary port number.
                                  # It is possible to register a protocol
                                  # with the IANA.  Such registered ports
                                  # are lower than 5000. e.g. HTTP (
                                  # for browser clients and web servers)
                                  # is registered by IANA as port 80
                                  #
                                  
            sock.settimeout(2.0) # create a 2 second timeout so that we
                                 # can use ctrl-c to stop a blocked server
                                 # if, for example, the client doesn't work.
            
            print ("UDP Server started on IP Address {}, port {}".format(IP,port))

            # Set up RSA key exchange
            rsa = RSA()

            MAX_PASSCODE = 2 ** 16

            RSA_transmitted = False
            # Wait for hello
            while not RSA_transmitted:
                try:
                  handshake_msg, source_address = sock.recvfrom(1024)
                  if handshake_msg.decode("UTF-8") == "Hey! Listen!":
                      rsa.from_message_bit_length(MAX_PASSCODE.bit_length(), 1)
                      #import pdb; pdb.set_trace()
                      public_key_text = str(rsa.public.modpq.MOD) + "|" + str(int(rsa.public.e))
                      sock.sendto(public_key_text.encode("UTF-8"), source_address)

                      RSA_transmitted = True
                except timeout:
                  continue
                

            # Set up RC4
            rc4 = None
            while rc4 is None:
                try:
                  # Now wait for the password
                  encrypted_password, source_address = sock.recvfrom(1024)

                  decrypted_password = rsa.private.decrypt(int(encrypted_password.decode("UTF-8")))
                  print("Password: {}".format(decrypted_password))

                  rc4 = RC4_Demo.Olin_RC4(str(decrypted_password).encode("UTF-8"))

                except timeout:
                  continue

            
            
            while True:
                try:
                    bytearray_encrypted, source_address = sock.recvfrom(1024) # 1024 is the buffer length
                                                                 # allocated for receiving the
                                                                 # datagram (i.e., the packet)
                                                                 
                    source_IP, source_port = source_address    # the source iaddress is ("127.0.0.1",client port number)
                                                               # where client port number is allocated to the TX process
                                                               # by the Linux kernel as part of the TX network stack))          
                    
                    print ("\nMessage received from ip address {}, port {}:".format(
                        source_IP,source_port))

                    bytearray_msg = rc4.crypt(bytearray_encrypted)


                    print (bytearray_msg.decode("UTF-8")) # print the message sent by the user of the  UDP_TX module.
                    
                    bytes_sent = sock.sendto(bytearray_encrypted, source_address) # this is the command to send the bytes in bytearray to the server at "Server_Address"

                    print ("{} bytes echoed to {}".format(bytes_sent, source_address))

                except timeout: 
                                
                    print (".",end="",flush=True)  # if process times out, just print a "dot" and continue waiting.  The effect is to have the server print  a line of dots
                                                   # so that you can see if it's still working.
                    continue  # go wait again

if __name__ == "__main__":
    Bob_Server()
