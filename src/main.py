import time
import os
import random
from qsieve import QS
from bruteforce import BF

def primesod(file):
    primeList = []
    for i in range (6):
        tempList = []
        for j in range(66):
            tempList.append(int(file.readline()))
        primeList.append(tempList)
    return primeList

def primes(file):
    primelist = []
    for i in range(462):
        num = int(file.readline())
        primelist.append(num)
    return primelist

pfile = open("primes.txt", "r")
pl = primes(pfile)
pr = len(pl)

def timeQS(n):
    initTime = time.time()
    b = 5000
    i = 5000

    issolve = QS(n, b, i)
    if issolve == "Error": return 0

    return time.time() - initTime

def timeBF(n):
    initTime = time.time()
    BF(n)

    return time.time() - initTime

#print(timeQS(1156643*2307517))

databf = open("src\databf.txt", "a")
dataqs = open("src\dataqs.txt", "a")

def runQS(toFile):
    trials = input()
    times = []
    nlist = []
    for i in range(int(trials)):
        p = pl[random.randint(0, pr - 1)]
        q = pl[random.randint(0, pr - 1)]
        n = p*q
        times.append(timeQS(n))
        nlist.append(n)
        print(i, "/", int(trials))

    for i in times:
        if toFile: 
            dataqs.write(str(i)) 
            dataqs.write("\n")
        else: print(str(i))

    for i in nlist:
        if toFile: 
            dataqs.write(str(i))
            dataqs.write("\n")
        else: print(str(i))

def runBF(toFile):
    trials = input()
    times = []
    nlist = []
    for i in range(int(trials)):
        p = pl[random.randint(0, pr - 1)]
        q = pl[random.randint(0, pr - 1)]
        n = p*q
        times.append(timeBF(n))
        nlist.append(n)
        print(i)

    for i in times:
        if toFile: 
            databf.write(str(i)) 
            databf.write("\n")
        else: print(str(i))

    for i in nlist:
        if toFile: 
            databf.write(str(i))
            databf.write("\n")
        else: print(str(i))

#runBF(True)
runQS(True)

databf.close()
dataqs.close()