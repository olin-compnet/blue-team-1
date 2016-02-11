import CN_Sockets
from rsa import RSA

# Client
socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout
MAX_PASSCODE = 2 ** 10

class ChatProgram(object):
    """docstring for ChatProgram"""
    def __init__(self, is_server=True):
        super(ChatProgram, self).__init__()
        self.is_server = is_server

    def server(self, IP="127.0.0.1", port=5280):
        rsa = RSA()
        rsa.from_message_bit_length(MAX_PASSCODE.bit_length())

        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.bind((IP, port))
            sock.settimeout(2.0)



            print("Chat Server started on {}:{}".format(IP, port))



    def send_public_key(self, public_key, address):
    

def public_key_text(public_key):
    return public_key_text = str(rsa.public.modpq.MOD) + "|" + str(rsa.public.e.value)
