from filehash import FileHash 


def hashFile(file):
    hashing=FileHash("sha256")
    d=hashing.hash_file(file)
    print(d)
    return d
    
#hashFile("/home/ayoub/devHacking/python/fileScan/jsfile.pdf")