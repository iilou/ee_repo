import math
from helpers import getPrimes

def BF(n):
    # if n < 7: return "Number %s too small" % n

    # primes = getPrimes(int(math.sqrt(n)))
    # for prime in primes:
    #     if n % prime == 0:
    #         return prime, int(n / prime)

    for i in range(2, n):
        if n % i == 0: return i
    return -1