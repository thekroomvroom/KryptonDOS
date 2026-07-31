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
    f"{sys.pm}@{sys.host}",
    f"Name: {sys.name}",
    f"Version: {sys.ver}",
    f"Version Codename: {sys.cn}",
    f"ID: {sys.id}",
    f"Host: {platform.system()} {platform.release()} {platform.version()}",
    f"CPU: {platform.processor()}",
    f"Random-Access Memory: {round(int(mem.used)/1000000000)}/{round(int(mem.total)/1000000000)} GB",
    f"Local Disk: {round(int(dsk.used)/1000000000)}/{round(int(dsk.total)/1000000000)} GB",
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