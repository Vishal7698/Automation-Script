import os
from sys import *
def Directry_wather(Path):
    flag=os.path.isabs(Path)

    if flag==False:
        Path=os.path.abspath(Path)

    exist=os.path.exists(Path)

    if exist:
        for foldername,subfolder,filename in os.walk(Path):
            print("current folder is "+foldername)
            for subf in subfolder:
                print("Subfolder of "+foldername+" is :"+subf)
            for filen in filename:
                print("file inside "+foldername+" is :"+filen)
    else:
        print("invalid path")

def main():
    print("Appliaction name is :"+argv[0])
    if len(argv)!=2:
        print("error: invalid number of argument")
        exit()
    try:
        Directry_wather(argv[1])
    except ValueError:
        print("invalid type of input")
    except Exception:
        print("invalid input")

if __name__=="__main__":
    main()