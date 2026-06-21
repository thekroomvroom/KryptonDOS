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

# IP Setup
rdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
adir = os.path.join(os.path.dirname(rdir), "app")

# Processing Data
torm = rmraw.split(" ")
amt = len(torm)

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

    # Integrity Check

    rkill = os.path.realpath(kill)
    rrdir = os.path.realpath(rdir)
    radir = os.path.realpath(adir)

    if rkill.startswith(rrdir + os.sep) or rkill.startswith(radir + os.sep) or rkill == rrdir or rkill == radir:
        print(f"era: {rkill if os.name == 'nt' else "C:" + rkill.replace("/", "\\")}; Hit Refused.")

    # Execute
    else:
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