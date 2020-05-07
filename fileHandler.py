# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:28:39 2020

@author: Ville Vainio
"""

import math

BYTE_COUNT_DECRYPT_CHUNK = 4
BYTE_COUNT_READ_CHUNK = 2

def saveKeyPair(e,d,n):
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
       
    return (n,e)

def readPrivKeyPair():
    privFile = "privateKey.txt"

    with open(privFile, 'r') as infile:
        string = infile.read()
        n,d = string.split()
        n = int(n)
        d = int(d)
        infile.close()

    return (n,d)

def encryptFileInChunks(path):
    f = open(path, 'rb')
    fileName = "encrypted-" + path
    print("Encrypting " + path + " to " + fileName)

    with open(fileName, 'wb') as outfile:
        while True:
            chunk = f.read(BYTE_COUNT_READ_CHUNK)
            if not chunk:
                break
            encrypted_data = encrypt(chunk)

            outfile.write(encrypted_data)
        f.close()
    outfile.close()
    return fileName

def decryptFileInChunks(path):
    f = open(path, 'rb')
    outFileName = "decrypted-" + path.replace('encrypted-','')
    print("Decrypting " + path + " to " + outFileName)

    with open(outFileName, 'wb') as outfile:
        while True:
            chunk = f.read(BYTE_COUNT_DECRYPT_CHUNK)
            if not chunk:
                break
            
            decrypted_data = decrypt(chunk)

            outfile.write(decrypted_data)
        f.close()

    outfile.close()

    return outFileName

# Encrypt binary data using public key
def encrypt(data_chunk):
    n,e = readPubKeyPair()
    chunk_int = bytesToInt(data_chunk)
    encrypted_int = pow(chunk_int, e, n)

    return intToBytes(encrypted_int, BYTE_COUNT_DECRYPT_CHUNK)

# Decrypt binary data using private key
def decrypt(encrypted_data_chunk):
    n,d = readPrivKeyPair()
    chunk_int = bytesToInt(encrypted_data_chunk)
    plain_text = pow(chunk_int, d, n)

    return intToBytes(plain_text)

def bytesToInt(raw_bytes: bytes) -> int:
    return int.from_bytes(raw_bytes, 'big', signed=False)

def intToBytes(number: int, fill_size: int = 0) -> bytes:
    if number < 0:
        raise ValueError("Number must be an unsigned integer: %d" % number)

    bytes_required = max(BYTE_COUNT_READ_CHUNK, math.ceil(number.bit_length() / 8))

    if fill_size > 0:
        return number.to_bytes(fill_size, 'big')

    return number.to_bytes(bytes_required, 'big')