import sys
import run

if len(sys.argv) ==1:
    print("""
Usage:
    brute.py <username> <passwordlist>          
          """)
    exit(0)

with open(sys.argv[2],"r") as file:
    for line in file.read().split("\n")[:-1]:
        print("Trying Passowrd {}".format(line))
        if run.login(sys.argv[1],line):
            print("Password found {}".format(line))
            exit(0)
        else:
            continue
    file.close()
