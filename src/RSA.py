import math
from lettertonumber import getEncodedMessage
n_key = 8633
d_key = 497
e_key = 17

message = getEncodedMessage()
print(message)

def encrypt(m, e, n):
    c = []
    for chunk in m:
        c.append((chunk**e) % n)
    return c

def decrypt(c, d, n):
    m = []
    for chunk in c:
        m.append((chunk**d) % n)
    return m

ciphertext = encrypt(message, e_key, n_key)
print(ciphertext)
deciphered = decrypt(ciphertext, d_key, n_key)
print(deciphered)