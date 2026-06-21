import sys
import os
import subprocess

sstruct = sys.argv[1]
todo = sys.argv[2]
cwd = sys.argv[3]
pwd = sys.argv[4]

dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dir")


try:
    sstructpath = os.path.join(dirpath, f"{sstruct}.py")
    if not os.path.exists(sstructpath):
        raise FileNotFoundError
    else:
        subprocess.run(["python3", sstructpath, todo, cwd, pwd])
except FileNotFoundError:
    sys.exit(1)
