# -*- coding: utf-8 -*-

import prime
import random
import math
import sys
import fileHandler

KEY_SIZE = 2048
BYTE_COUNT_READ_CHUNK = int((KEY_SIZE // 8) - 1) #encrypt 1024/8 - 1 bytes at a time
BYTE_COUNT_DECRYPT_CHUNK = KEY_SIZE # keysize in bits

# Generate k-bit RSA public/private key pair
def generate_key_pair(keysize):
    #generate p and q which are primes and not equal
    p = prime.generate_primes(n=int(keysize/2), k=1)[0]
    q = prime.generate_primes(n=int(keysize/2), k=1)[0]

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
    n,e = fileHandler.readPubKeyPair()
    chunk_int = bytesToInt(data_chunk)
    encrypted_int = pow(chunk_int, e, n) # result <= n

    return intToBytes(encrypted_int, BYTE_COUNT_DECRYPT_CHUNK)

# Decrypt binary data using private key
def decrypt(encrypted_data_chunk):
    n,d = fileHandler.readPrivKeyPair()
    chunk_int = bytesToInt(encrypted_data_chunk)
    plain_text = pow(chunk_int, d, n)

    return intToBytes(plain_text)

def bytesToInt(raw_bytes: bytes) -> int:
    return int.from_bytes(raw_bytes, 'big', signed=False)

def intToBytes(number: int, fill_size: int = 0) -> bytes:
    if number < 0:
        raise ValueError("Number must be an unsigned integer: %d" % number)

    bytes_required = max(fill_size, math.ceil(number.bit_length() / 8))

    return number.to_bytes(bytes_required, 'big')

def initKeys():
    e,d,n = generate_key_pair(KEY_SIZE)
    fileHandler.saveKeyPair(e,d,n)

def main():
    initKeys()
    if len(sys.argv) != 2:
        print("Incorrect program arguments. Expected invocation: python RSA.py file_path")
        exit()
    encrypted_file_path = encryptFileInChunks(sys.argv[1])
    decryptFileInChunks(encrypted_file_path)

if __name__ == "__main__":
    main()