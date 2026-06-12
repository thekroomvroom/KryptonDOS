import os
import sys
import shutil

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

rmraw = sys.argv[1]
dirat = sys.argv[2]

if " " in rmraw:
    torm = rmraw.split(" ")
    amt = len(torm)
else:
    torm = rmraw
    amt = 1

for i in range(int(amt)):
    kls = torm[int(i)]
    cwd = dirat

    if os.name == 'nt':
        if ":\\" in kls:
            kill = kls
        else:
            kill = os.path.join(cwd, kls)
    else:
        if kls.startswith("C:\\"):
            kill = kls[2:].replace("\\", "/")
        else:
            kill = os.path.join(cwd, kls)

    try:
        if os.path.isfile(kill):
            os.remove(kill)
            print("Operation Success.")
        elif os.path.isdir(kill):
            shutil.rmtree(kill)
            print("Operation Success.")
        else:
            print("Specified File or Directory Does Not Exist.")
    except Exception as e:
        print(e) 