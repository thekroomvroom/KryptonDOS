import sys
import os
import subprocess

sstruct = sys.argv[1]
todo = sys.argv[2]
cwd = sys.argv[3]
pwd = sys.argv[4]

timepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "time")

try:
    sstructpath = os.path.join(timepath, f"{sstruct}.py")
    if not os.path.exists(sstructpath):
        raise FileNotFoundError
    else:
        subprocess.run(["py" if os.name == 'nt' else "python3", sstructpath, todo, cwd, pwd, timepath])
except FileNotFoundError:
    sys.exit(1)
