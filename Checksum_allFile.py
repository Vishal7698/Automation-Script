from sys import *
import os
import hashlib


def Hashfile(path,BLOCKSIZE=1024):
    hasher=hashlib.md5()
    file=open(path,'rb')
    buf=file.read(BLOCKSIZE)

    if len(buf)>0:
        hasher.update(buf)
        buf=file.read(BLOCKSIZE)

    file.close()
    return hasher.hexdigest()

def Display_checksum(path):
    dict={}
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exist=os.path.isdir(path)

    if exist:
        for Directory_name,Sub_directory,Filename_List in os.walk(path):
            print("Current folder is "+Directory_name)
            for file in Filename_List:
                path=os.path.join(Directory_name,file)
                hashvalue=Hashfile(path)

                if file in dict:
                    pass
                else:
                    dict[file]=hashvalue

    return dict



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
        checksum=Display_checksum(argv[1])

        for file,value in checksum.items():
            print("checksum of file {} is {}".format(file,value))
    except ValueError:
        print("enter valid input")
    except Exception:
        print(Exception)



if __name__=="__main__":
    main()