#import libraries
import os
import datetime
import json
from pathlib import Path

#dec f
sysn = "nt" if os.name == 'nt' else "unix"

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

odir = os.path.dirname(os.path.abspath(__file__))
rdir = os.path.dirname(os.path.dirname(odir))
secdir = os.path.join(rdir, "sec")
currdir = Path.cwd()

infpath = os.path.join(secdir, "inf.json")
with open(infpath, "r") as f:
    inf = json.load(f)

class sys:
    name = inf["name"]
    id = inf["id"]
    cn = inf["codename"]
    ver = inf["version"]
    knl = inf ["kernel"]
    pm = inf["pm"]
    host = inf["host"]

#main
print()
print(f"Volume in drive \"C:\":")
print(f"Directory of C:{str(currdir).replace("/", "\\")}")
print()

files = 0
dirs = 0
total_bytes = 0

for item in os.listdir("."):

    stats = os.stat(item)

    modified = datetime.datetime.fromtimestamp(stats.st_mtime)
    time_str = modified.strftime("%m-%d-%Y  %I:%M%p")

    if os.path.isdir(item):
        print(f"{item:<12} <DIR>    {time_str}")
        dirs += 1
    else:
        print(f"{item:<12} {stats.st_size:>8} {time_str}")
        files += 1
        total_bytes += stats.st_size

print()
print(f"{files} file(s) {total_bytes:,} bytes")
print(f"{dirs} dir(s)")
print()