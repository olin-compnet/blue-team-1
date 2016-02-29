from receivemorse import receive_morse as receive
from BlinkTX import send_morse as send
import sys
# Determine own IP Address

class DataLinkLayer:
    def __init__(self, address):
        self.address = address # Determine ourselves
        self.receive_generator = receive()

    def check_sum(self):
        pass

    def send(self, destination, payload):
        msg = " ".join([destination, self.address, payload]) # Clever code, hate me later
        send(msg)

    def receive(self):
        msg = self.receive_generator.__next__()
        dst, src, payload = msg.split(" ", maxsplit=2)
        if self.address == dst:
            # Do something with payload
            print("From:", src, ">", payload, sep=" ")
            return (src, payload)


if __name__ == "__main__":
    address = sys.argv[1]
    dll = DataLinkLayer(address)
    while True:
        dll.receive()
