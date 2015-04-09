import random
import math

def writeRow(i, a, q, x, y, string):
    print string.format(i, a, q, x, y) 

def extEuclid(a01, a02, modulus=False):
    string = ("| {:>" + str(max(2, len(str(a01)))) + "} ")*5 + "|"
    i = 0
    a1, a2 = a01, a02
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    q = 0

    writeRow("i", "ai", "Q", "xi", "yi", string)
    writeRow(i, a1, "-", x1, y1, string)
    i += 1
    q = a1/a2
    writeRow(i, a2, q, x2, y2, string)

    while (a2 != 0):
        i += 1
        
        t = a2
        a2 = (a1 - q*a2)
        if (modulus):
            a2 %= a01
        a1 = t

        if (a2 != 0):
            t = x2
            x2 = (x1 - q*x2)
            if (modulus):
                x2 %= a01
            x1 = t

            t = y2
            y2 = (y1 - q*y2)
            if (modulus):
                y2 %= a01
            y1 = t
            
            q = a1/a2
            
            writeRow(i, a2, q, x2, y2, string)
        else:
            writeRow(i, a2, "", "", "", string)
    result = a01*x2+a02*y2
    if (modulus):
        result %= a01
    print "{} * {} + {} * {} = {}".format(a01, x2, a02, y2, result)
    return result, x2, y2

def factorize(n):
    def isPrime(n):
        return not [x for x in xrange(2,int(math.sqrt(n)))
                    if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1            
    return primes

def condense(L):
  prime,count,list=0,0,[]
  for x in L:
    if x == prime:
      count = count + 1
    else:
      if prime != 0:
        list = list + [str(prime) + '^' + str(count)]
      prime,count=x,1
  list = list + [str(prime) + '^' + str(count)]
  return list
    

### GF(n) functions
def modInverse(n, t):
    tt, x1, x2 = extEuclid(n, t, modulus=True)
    if (t*x2 % n == 1):
        print "{}^-1 = {} mod {}".format(t, x2, n)
        return x2
    else:
        print "Something goes wrong: {} * {} = {}".format(t, x2, t*x2 % n)
        return None

def mod(a, n):
    result = a%n
    print "{} = {} mod {}".format(a, result, n)
    return result

def modPow(a, x, n):
    result = (a**x)%n
    print "{}^{} = {} mod {}".format(a, x, result, n)
    return result


### CIPHERS
def RSACipher():
    def showHelp():
        print '''Functions of RSA cipher:
        0 - Encrypt
        1 - Decrypt
        2 - Crack
            0 - Factorize N

        h - Help
        x - Exit'''

    showHelp()
    while (True):
        command = str(raw_input("\n[RSACipher] Enter command: ")).strip()
        if (command == "0"):
            pass
        if (command == "1"):
            pass
        elif (command == "2"):
            pass

        elif (command == "h"):
            showHelp()
        elif (command == "x"):
            break
        else:
            print "Unknown command"


### MAIN
def showHelp():
    print '''Functions:
    0 - a mod n
    1 - mod pow
    2 - Extended Euclid
    3 - Inverse element
    4 - Factorization
    5 - RSA cipher crypt/decrypt/crack
    To Be Continued

    h - Help
    x - Exit'''
# TODO:
# additive cipher crypt/decrypt/crack
# affine cipher crypt/decrypt/crack
# permutation cipher crypt/decrypt/crack
# GF(p^n) polynom math
#   (found primitive, brute roots, mult/div/add/subtr, modPow...)
# found rang of element in field
#   (factorize n-1 and found the x:
#       a^x = 1 mod n
#       n-1%x = 0
#       x < y for y: y!=x, n-1%y = 0
# build field GF(p^n)
# LFSR...

showHelp()
while (True):
    command = str(raw_input("\nEnter command: ")).strip()
    if (command == "0"):
        n = int(input("mod = "))
        t = int(input("a = "))
        mod(t, n)
    elif (command == "1"):
        n = int(input("mod = "))
        t = int(input("a = "))
        x = int(input("x = "))
        modPow(t, x, n)
    elif (command == "2"):
        n = int(input("a0 = "))
        t = int(input("a1 = "))
        extEuclid(n, t)
    elif (command == "3"):
        n = int(input("mod = "))
        t = int(input("a = "))
        modInverse(n, t)
    elif (command == "4"):
        x = int(input("x = "))
        print ", ".join(condense(factorize(x)))
    elif (command == "5"):
        RSACipher()

    elif (command == "h"):
        showHelp()
    elif (command == "x"):
        break
    else:
        print "Unknown command"

