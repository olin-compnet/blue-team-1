#Alexander Hoppe
#alexander.hoppe@students.olin.edu
#2/1/16
from fractions import gcd
import primetools
PT = primetools.primetools()
"""
Implementation of RSA public-private key encryption for Computer Networks SP16

Inspired by Alex Morrow's OlinRSA implementation
"""
# implementation for mod. mult. inverse from Wikipedia
def modular_multiplicative_inverse(a, n):
    t = 0
    nt = 1
    r = n
    nr = a % n
    if n < 0:
        n = -n
    if a < 0:
        a = n - (-a % n)
    while not nr == 0:
        quot = (r//nr) | 0
        tmp = nt; nt = t - quot*nt; t = tmp;
        tmp = nr; nr = r - quot*nr; r = tmp;
    if r > 1:
        return -1
    if t < 0:
        t += n
    return t

def mod_exp(base, exp, mod):
    return math.pow(base, exp) % mod

class RSA:

    # Generate keys, based on P and Q, arbitrary random primes that are big.
    def __init__(self, message_bit_length=8):

        startp = 2**message_bit_length

        P = Q = E = None
        for P in range(startp,startp+100): # to be randomized
            if PT.prime(P):
                p = P # found a prime!
                break
                if not P:ValueError("Prime p not found")

        for Q in range(startp+200,startp+300):# to be randomized
            if PT.prime(Q):
                q = Q
                break
                if not q: ValueError("prime q not found")

        n = p*q
        phi = (p-1)*(q-1)
        e = 2**16 + 1
        while gcd(e, phi) > 1:
            e += 1

        # public and private key classes
        self.public = RSA_Public(n, e)
        self.private = RSA_Private(p, q, e)

# Holds onto public keys and encrypt method
class RSA_Public:

    def __init__(self, n, e):
        self.n = n
        self.e = e

    def authenticate(self):
        return self.encrypt(signature) == receivedtext

    def encrypt(self, m, dest_public):
        n, e = dest_public
        return m**e % n

    def import_public_key(self, public_key):
        pubkeyparse = public_key.split("\n")
        if pubkeyparse[0] != "Alexander Hoppe" or pubkeyparse[1] != "Olin College CompNet RSA Model":
            raise ValueError("Invalid public key:{}".format(pubkey))
        self.n = int(pubkeyparse[2])
        self.e = int(pubkeyparse[3])
        return

    def export_public_key(self):
        pubkey = """\
Alexander Hoppe
Olin College CompNet RSA Model
{}
{}
""".format(self.n,self.e)
        return pubkey

# Holds onto private key, decrypt  method, and sign.
class RSA_Private:

    def __init__(self, p, q, e):
        phi = (p-1)*(q-1)
        self.d = modular_multiplicative_inverse(e, phi)
        self.n = p*q

    def decrypt(self, ciphered_m):
        return pow(ciphered_m,self.d,self.n)


if __name__ == '__main__':
    alice = Hoppe_RSA(61, 53)
    bob = Hoppe_RSA(97, 61)

    print('encrypting 65')
    m = alice.encrypt(65, bob.public)
    print(m)
    decoded = bob.decrypt(m)
    print('result = ' + str(decoded))
