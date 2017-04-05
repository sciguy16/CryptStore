import hashlib

def GenerateKey(length, *args):
    assert(length > 0)
    assert(length <= 256)

    #Generate hash
    m = hashlib.sha256()
    for i in args:
        m.update(i.encode('utf-8'))
    key = m.hexdigest()

    #Generate mask
    mask = 0
    for i in range(0,length):
        mask |= (1<< i)

    #Return key
    return (int(key,16) & mask)


print(GenerateKey(256,"Josh","is", "Very cool"))