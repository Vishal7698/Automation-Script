"""Automation using Python
    Automation is consider as process which executes certain task without any human
    interaction.
    By using the automation technique we can automate multiple tasks as
    •    Moving , renaming or deleting files
    • Downloading multiple files
    • Updating and searching in files
    • Sending and receiving mails
    • Schedule task through the process
    We can perform this kind of Automations by using Python.
    We are going to follow some rules while writing Automation Scripts as
    • Accept input through command line or through file.
    • Display any message in log file instead of console.
    • For separate task define separate function.
    •   For robustness handle every expected exception.
    • Perform validations before taking any action.
    • Create user defined modules to store the functionality."""

from sys import *

def fun(parameter):
    print(parameter)

def main():
    print("aplication name "+argv[0])

    if len(argv)<3:
        print("Error invalid number of argument")

    if argv[1]=='-h':
        print("this script design for")
    if argv[1]=='-u':
        print("this script is design for ")

    try:
        fun(argv[1])
    except Exception as e:
        print("error"+e)

if __name__=="__main__":
    main()