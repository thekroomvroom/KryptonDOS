import os
import psutil
import platform
import json

odir = os.path.dirname(os.path.abspath(__file__))
rdir = os.path.dirname(os.path.dirname(odir))
secdir = os.path.join(rdir, "sec")

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

mem = psutil.virtual_memory()
dsk = psutil.disk_usage('/')
print()

ascii_art = """
 █████   ████          
░░███   ███░           
 ░███  ███    ████████ 
 ░███████    ░░███░░███
 ░███░░███    ░███ ░░░ 
 ░███ ░░███   ░███     
 █████ ░░████ █████    
░░░░░   ░░░░ ░░░░░     
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
""".splitlines()

specs = [
    f"\033[1;4m{sys.pm}@{sys.host}\033[0m\n",
    f"\033[1mName:\033[0m {sys.name}",
    f"\033[1mVersion:\033[0m {sys.ver}",
    f"\033[1mVersion Codename:\033[0m {sys.cn}",
    f"\033[1mID:\033[0m {sys.id}",
    f"\033[1mHost:\033[0m {platform.system()} {platform.release} {platform.version}",
    f"\033[1mCentral Processing Unit:\033[0m {platform.processor}",
    f"\033[1mRandom-Access Memory:\033[0m {round(int(mem.used)/1000000000)}/{round(int(mem.total)/1000000000)} GB",
    f"\033[1mLocal Disk:\033[0m {round(int(dsk.used)/1000000000)}/{round(int(dsk.total)/1000000000)} GB",
    " ",
    " ",
]

# Pad ascii art to match info length and vice versa
width = max(len(line) for line in ascii_art)
ascii_art = [line.ljust(width) for line in ascii_art]

# Zip together and print side by side
for left, right in zip(ascii_art, specs):
    print(f"{left}   {right}")

print()