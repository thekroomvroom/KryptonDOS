import os
import sys

todo = sys.argv[1]
cwd = sys.argv[2]

if ">>" in todo or " >> " in todo:
    inj = todo.split(">>")
    for i in range(len(inj)):
        print(f"{inj[int(i)]} ", end="") 

os.system("echo python is a bitch")