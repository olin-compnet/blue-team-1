#
## Test 
#

input("enter when ready")

import time
import traceback
import socket as socket_module
        
class testudp:

    class socket(socket_module.socket):
       
    
        def __exit__(self,etype,value,tb):
            self.close() # close socket
            if etype == value == tb == Null:
                print("OK")
                print("normal end")
                input("enter when ready to quit")
                return True
            else:
                print("failure")
                self.close()
                
                print("etype = {}({})".format(etype,value))
                print("traceback ",60*"-")
                traceback.print_exception(etype,value,tb)
                print("          ",60*"-")
                #print("traceback = {}".format(traceback(print_tb(etraceback))))
                input("enter when ready to quit")
                return False
    
    def __init__(self,port=12341,timeout=0.1, maxseconds=60):
        self.port = port
        self.timeout = timeout
        self.maxseconds = maxseconds
        self.localhost = "127.0.0.1"
        self.server_address = (self.localhost,self.port)
        
    def server(self):
    
        with self.socket(2,2) as sock:
            sock.settimeout(self.timeout)
            sock.bind(self.server_address)
            while True:
                msg, addr = self.recv(sock)
                print("inbound bytes: {} from client {}".format(msg, addr))
                print("echo back {} bytes".format(self.send(sock,msg,addr)))
                
            
    def client(self,prompt):
        
            with self.socket(2,2) as sock:
                sock.settimeout(self.timeout)
                while True:
                    input_message = input(prompt)
                    print("input message: {}".format(input_message))
                    print("input message length: {}".format(len(input_message)))
                    utf8_input_message = input_message.encode()
                    print("UTF-8 encode: {}".format(utf8_input_message))
                    #time.sleep(10)
                    print("{} bytes sent to address {}".format(self.send(sock,utf8_input_message,self.server_address),self.server_address))
                    print("bytes received: {}".format(self.recv(sock)))
                    
            
    def send(self,sock,m,a):
        t0 = time.time()
        toc = 0
        while time.time()-t0 < self.maxseconds:
            try:
                ct = sock.sendto(m,a)
                return ct
            except socket_module.timeout as sto:
                toc +=1
                continue
            except KeyboardInterrupt as kbi:
                raise KeyboardInterrupt
        raise TimeoutError("Maxseconds betweem messages  expired")
            
            
    def recv(self,sock):
        t0 = time.time()
        toc = 0


        
        while time.time()-t0 < self.maxseconds:
            try:
                return sock.recvfrom(1600)    
            except socket_module.timeout as sto:
                toc +=1
                continue
            except KeyboardInterrupt as kbi:
                raise KeyboardInterrupt

            
    
    
    
            
                

           
                
                
                
