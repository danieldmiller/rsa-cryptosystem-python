# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import prime
import random
import fileHandler

# Generate k-bit RSA public/private key pair
def generate_key_pair(keysize):
    #generate p and q which are primes and not equal
    while True:
        p=prime.initPrimes()
        q=prime.initPrimes()
        if(p!=q):
            break

    n = p*q
    
    phi = (p-1) * (q-1)
    
    #verify copmprime
    while True:
        e = random.randint(1, phi)
        g = prime.gcd(e,phi)
        if(g == 1):
            break

    #generate private key
    d = prime.euclidAlgorithm(e, phi)
    
    return (e,d,n)

def initKeys():
    key_size = 1024
    e,d,n = generate_key_pair(key_size)
    fileHandler.saveKeyPair(e,d,n)

def main():
    initKeys()
    encrypted_file_path = fileHandler.encryptFileInChunks("file.jpg")
    fileHandler.decryptFileInChunks(encrypted_file_path)

if __name__ == "__main__":
    main()
