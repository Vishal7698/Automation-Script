"""Automation Script which accept the path of dictonary from user and display all name of duplicate file from
dictonary"""

import os
from sys import *
import hashlib
"""For generating python secure hash message, we need to use hashlib module. Python hashlib hashing function takes
 variable length of bytes and converts it into a fixed length sequence. This is a one way function. That means, you 
 hash a message, you get a fixed length sequence."""

def hashfile(path,blocksize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=fd.read(blocksize)

    fd.close()
    return  hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exist=os.path.exists(path)

    dups={}
    if exist:
        for dirname,subdir,fileList in os.walk(path):
            for filen in fileList:
                path=os.path.join(dirname,filen)
                file_hash=hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]

        return dups
    else:
        print("error invalid path")

def PrintDub(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("duplicate found")

        print("following files are identical")

        icnt=0
        for result in results:
            print("###########################")
            for subresult in result:
                icnt+=1
                if icnt >=2:
                    print('\t\t%s'%subresult)

def main():
    print("welcome to Application")
    print("application name is "+argv[0])

    if (len(argv)!= 2):
        print("ERROR: invalid number of argumnet")
        exit()

    if(argv[1]=='h') or (argv[1]=='H'):
        print("this script is use to transver the specific directry and display size of files")
        exit()

    if (argv[1]=='u') or (argv[1]=='U'):
        print("usage : apsolute path  of directory extension")
        exit()

    try:
        arr={}
        arr=FindDuplicate(argv[1])
        PrintDub(arr)

    except ValueError:
        print("invalid type of input")

if __name__=="__main__":
    main()