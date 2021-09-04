import math
from helpers import getPrimes

def BF(n):
    if n < 7: return "Number %s too small" % n

    primes = getPrimes(int(math.sqrt(n)))
    for prime in primes:
        if n % prime == 0:
            return prime, int(n / prime)