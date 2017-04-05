# Adapted from http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto

import os, random, struct
from Crypto.Cipher import AES

import tempfile
import tarfile

chunksize=64*1024 #Always use this chunksize

def getFileSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    fileobject.seek(0, )  # move the cursor to the beginnning of the file
    return size

def encrypt_file(key, infile, outfile, chunksize):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        infile/outfile:
            input/output file

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    iv = bytes([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    encryptor = AES.new(key, AES.MODE_CBC, iv)

    filesize = getFileSize(infile)

    outfile.write(struct.pack('<Q', filesize))
    outfile.write(iv)

    while True:
        chunk = infile.read(chunksize)
        if len(chunk) == 0:
            break
        elif len(chunk) % 16 != 0:
            chunk += (' ' * (16 - len(chunk) % 16)).encode('utf-8')

        outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, infile, outfile, chunksize):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file
    """

    origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
    iv = infile.read(16)
    decryptor = AES.new(key, AES.MODE_CBC, iv)


    while True:
        chunk = infile.read(chunksize)
        if len(chunk) == 0:
            break
        outfile.write(decryptor.decrypt(chunk))

    outfile.truncate(origsize)


def encrypt(key, input_filename, output_filename):
    isfolder = os.path.isdir(input_filename)
    print(isfolder)
    if isfolder:
        #Create tar of directory in RAM
        tmp = tempfile.TemporaryFile()
#        tarhandle = tarfile.open(fileobj=tmp, mode='w:')
        tarhandle = tarfile.open("test.tar", "w")
        tarhandle.add(input_filename, '.')
        tarhandle.close()
        tmp.flush()
        tmp.seek(0)
        infile = tmp

    else:
        infile = open(input_filename, 'rb')

    outfile = open(output_filename, 'wb')
    encrypt_file(key, infile, outfile, chunksize)

    if isfolder:
        return 'folder'
    else:
        return 'file'


def decrypt(key, input_filename, output_filename):
    input = open(input_filename, 'rb')
    output = open(output_filename, 'wb')
    decrypt_file(key, input, output, chunksize)


key = '0123456789abcdef'
#plaintext = "plaintext.txt"
plaintext = "./test_files"
cyphertext = "cyphertext.txt"
plaintext_out = "plaintext_out.txt"

encrypt(key, plaintext, cyphertext)

decrypt(key, cyphertext, plaintext_out)

#Check input and output are identical
import filecmp
assert(filecmp.cmp(plaintext, plaintext_out))
