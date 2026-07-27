import sys
import os
import subprocess

print("net is still under-contruction, it is advisable not to use it right now! ")

sstruct = sys.argv[1]
todo = sys.argv[2]
cwd = sys.argv[3]

dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "internal")

try:
    sstructpath = os.path.join(dirpath, f"{sstruct}.py")
    if not os.path.exists(sstructpath):
        raise FileNotFoundError
    else:
        subprocess.run(["python3", sstructpath, todo, cwd])
except FileNotFoundError:
    sys.exit(1)
