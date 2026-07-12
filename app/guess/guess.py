import sys
import os
import subprocess
import time
import random

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

sstruct = sys.argv[1]
todo = sys.argv[2]

if not sstruct == '':
    sys.exit(1)
else:
    odir = os.path.dirname(os.path.abspath(__file__))
    idir = os.path.join(odir, "internal")

    gamepath = os.path.join(idir, "game.py")

    time.sleep(random.uniform(0.1, 3))
    clear()

    subprocess.run(["python3", gamepath])