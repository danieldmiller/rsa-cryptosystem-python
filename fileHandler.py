# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:28:39 2020

@author: Ville Vainio
"""

def saveKeyPair(e,d,n):
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

def encryptFileInChunks(path):
    f = open(path, 'rb')
    fileName = "encrypted-" + path
    print("Encrypting " + path + " as " + fileName)

    with open(fileName, 'w') as outfile:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break

            encrypted_data = encrypt(chunk)
            outfile.write(str(encrypted_data))
        f.close()

    outfile.close()
    return fileName

def decryptFileInChunks(path):
    f = open(path, 'rb')
    fileName = "decrypted-" + path.replace('encrypted-','')
    print("Decrypting " + path + " as " + fileName)

    with open(fileName, 'w') as outfile:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break

            decrypted_data = decrypt(chunk)
            outfile.write(str(decrypted_data))
        f.close()

    outfile.close()
    return fileName

# Encrypt binary data using public key
def encrypt(data_chunk):
    e,n = readPubKeyPair()
    chunk_int = int.from_bytes(data_chunk, byteorder='big', signed=False)
    cipher_text = pow(chunk_int, e, n)
    return cipher_text

# Decrypt binary data using private key
def decrypt(encrypted_data_chunk):
    d,n = readPrivKeyPair()
    chunk_int = int.from_bytes(encrypted_data_chunk, byteorder='big', signed=False)
    plain_text = pow(chunk_int, d, n)
    
    return plain_text
