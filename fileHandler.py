# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:28:39 2020

@author: Ville Vainio
"""

import rsa


def saveKeyPair():
    keysize = 1024
    print('Generating %i-bit key' % keysize)
    e,d,n = rsa.generate_key_pair(keysize)
    #(pub_key, priv_key) = rsa.generate_key_pair(keysize)
    fileName = "publicKey.txt"
    print('Writing public key to %s' % fileName)
    with open(fileName, 'w') as outfile:
       #pub_key has attributes: n: int, e: int
       outfile.write(str(n))
       outfile.write("    ") # seperating n and e
       outfile.write(str(e))
       outfile.close()

    fileName = "privateKey.txt"
    print('Writing private key to %s' % fileName)
    with open(fileName, 'w') as outfile:
       # priv_key has attributes: n: int, e: int, d: int, p: int, q: int
       outfile.write(str(n))
       outfile.write("    ") # seperating n and e
       outfile.write(str(d))

def readPubKeyPair():
    
    pubFile = "publicKey.txt"

    with open(pubFile, 'r') as infile:
       string = infile.read()
       n,e = string.split()
       #pub_key has attributes: n: int, e: int
       n = int(n)
       e = int(e)
       infile.close()
       
    return (e,n)

def readPrivKeyPair():
    privFile = "privateKey.txt"
    
    with open(privFile, 'r') as infile:
        string = infile.read()
        n,d = string.split()
        n = int(n)
        d = int(d)
        infile.close()
    
    return (d,n)