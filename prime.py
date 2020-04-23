# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import random

    
def initPrimes() -> int:
    minPrime = 2**1023
    maxPrime = (2**1024 - 1)

    while True:
        prime = random.randint(minPrime,maxPrime)
        if(isPrime(prime)):
           break

    return prime


def isPrime(x) -> bool:
    for i in range(2,x):
       if (x % i) == 0:
           return 0
       else:
           return 1
               
       
        
def gcd(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# ax+by=gcd(a,b).
def euclidAlgorithm(a,b):
    # r = gcd(a, b) = xa + yb
    #x = multiplicitive inverse of a mod b
    # y = multiplicitive inverse of b mod a
    x = 0
    xx = 1
    ob = b
    while b!=0:
        q = a//b
        r = a%b
        (a, b) = (b, r)
        (x, xx) = ((xx - (q * x)), x)
    
    if xx < 0: #if negative wrap with original value b
        xx += ob
        
    return xx
        

def printN():
    print(initPrimes())

