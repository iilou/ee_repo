import time
import random
from qsieve import QS
from bruteforce import BF

def primesod(file):
    primeList = []
    for i in range (7):
        tempList = []
        for j in range(66):
            tempList.append(int(file.readline()))
        primeList.append(tempList)
    return primeList

def primes(file):
    primelist = []
    rg = int(file.readline())
    for i in range(rg):
        num = int(file.readline())
        primelist.append(num)
    return primelist

pfile = open("primes.txt", "r")
spfile = open("primessmall.txt", "r")
lpfile = open("primeslarge.txt", "r")
pl = primes(pfile)
pr = len(pl)

def getn():
    p = random.randint(0, pr-1)
    q = p
    while p == q: q = random.randint(0, pr-1)
    return pl[p] * pl[q]

def timeQS(n):
    initTime = time.time()

    blist = [1000, 2000, 3000, 4000, 5000, 7500, 10000, 12500, 15000, 17500, 20000, 25000, 30000, 40000, 50000, 60000, 70000, 80000]

    b = 4000
    i = 4000

    for bv in blist:
        if QS(n, bv, bv) != "Error": 
            print(n, "~~~", bv)
            break
        initTime = time.time()
        if bv == 50000: return -1

    return time.time() - initTime

def timeBF(n):
    initTime = time.time()
    BF(n)

    return time.time() - initTime

#print(timeQS(1156643*2307517))

databft = open("src\databft.txt", "w")
databfn = open("src\databfn.txt", "w")
dataqst = open("src\dataqst.txt", "w")
dataqsn = open("src\dataqsn.txt", "w")

def runQS(toFile):
    trials = input()
    times = []
    nlist = []
    for i in range(int(trials)):
        n = getn()
        times.append(timeQS(n))
        nlist.append(n)
        print(i, "/", int(trials))

    for i in times:
        if toFile: 
            dataqst.write(str(i)) 
            dataqst.write("\n")
        else: print(str(i))

    for i in nlist:
        if toFile: 
            dataqsn.write(str(i))
            dataqsn.write("\n")
        else: print(str(i))

def runBF(toFile):
    trials = input()
    times = []
    nlist = []
    for i in range(int(trials)):
        n = getn()
        times.append(timeBF(n))
        nlist.append(n)
        print(i, "/", int(trials))

    for i in times:
        if toFile: 
            databft.write(str(i)) 
            databft.write("\n")
        else: print(str(i))

    for i in nlist:
        if toFile: 
            databfn.write(str(i))
            databfn.write("\n")
        else: print(str(i))

if input() == "b": runBF(True)
if input() == "q": runQS(True)

databft.close()
databfn.close()
dataqst.close()
dataqsn.close()