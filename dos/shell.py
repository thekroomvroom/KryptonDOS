# import libraries #
import os
import time
import json
import random
import subprocess
import sys as lsys
from pathlib import Path

# Declaring functions and variables pre-program
sysn = "nt" if os.name == 'nt' else "unix"

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

odir = os.path.dirname(os.path.abspath(__file__))

cmddir = os.path.join(odir, "cmd")
infpath = os.path.join(os.path.join(odir, "sec"), "inf.json")
with open(infpath, "r") as info:
    inf = json.load(info)

class sys:
    name = inf["name"]
    id = inf["id"]
    cn = inf["codename"]
    ver = inf["version"]
    knl = inf ["kernel"]
    pm = inf["pm"]
    host = inf["host"]

loop = True
err = False
pwd = None
cwd = "C:\\"
runtimelog = None

# main

while loop == True:

    err = False
    runtimelog = None
    # Store Previous Working Directory
    pwd = cwd

    # Get Current Path
    cwd = Path.cwd()

    if os.name == 'nt':
        cdir = cwd
    else:
        cdir = "C:" + str(cwd).replace("/", "\\")

    # Input
    print(f"{sys.name}@{sys.host}: {cdir}>", end="")
    cmd = input("")

    
    # Parse
    parts = cmd.split(" ", 1)

    istruct = parts[0]
    try:
        todo = parts[1]
    except Exception:
        todo = ""

    if "." in  istruct:
        parts = istruct.split(".", 1)
        mstruct = parts[0]
        sstruct = parts[1]
    else:
        mstruct = istruct
        sstruct = ""

    # Execute

    # MISC
    if mstruct == 'exit':
        if sstruct != '' or todo != '':
            err = True
        else:
            print("Quitting Shell..."); time.sleep(random.uniform(0.1, 3))
            clear()
            loop = False
    elif mstruct == 'reboot':
        if sstruct != '' or todo != '':
            err = True
        else:
            print("Rebooting Shell..."); time.sleep(random.uniform(0.1, 3)); clear()
            shellpath = os.path.join(odir, "shell.py")
            os.execv(lsys.executable, [lsys.executable, shellpath])
    elif mstruct == 'cls':
        if sstruct != '' or todo != '':
            continue
        else:
            clear()

    # CD
    elif mstruct == 'cd':
        if "/" in todo:
            print("Directory Specified Does Not Exist")
        elif sstruct == 'back':
            try:
                os.chdir(pwd)
            except Exception:
                print("Directory Specified Does Not Exist.")
        elif sstruct == '':
            if todo == '..':
                try: 
                    os.chdir(os.path.dirname(cwd))
                except Exception:
                    print("Directory Specified Does Not Exist.")
            elif todo == '..\\..':
                try:
                    os.chdir(os.path.dirname(os.path.dirname(cwd)))
                except Exception:
                    print("Directory Specified Does Not Exist.")
            else:
                if os.name == 'nt':
                    if todo.startswith("C:\\"):
                        tocd = todo
                    else:
                        os.path.join(cwd, todo)

                else:
                    if todo.startswith("C:\\"):
                        tocd = todo[3:].replace("\\", "/")
                    else:
                        tocd = os.path.join(cwd, todo)
    
                try:
                    os.chdir(tocd)
                except Exception:
                    print("Directory Specified Does Not Exist.")
        else:
            err = True
    
    # Main CMD
    else:
        try:
            mdir = os.path.join(cmddir, f"{mstruct}.py")

            if not os.path.exists(mdir):
                raise FileExistsError
            else:
                runtimelog = subprocess.run(["py" if os.name == 'nt' else "python3", mdir, sstruct, todo, cwd, pwd])
        except FileExistsError:
            try:
                appdir = os.path.join(os.path.dirname(odir), "app")
                mdir = os.path.join(appdir, mstruct)
                apppath = os.path.join(mdir, f"{mstruct}.py")
                if not os.path.exists(apppath):
                    raise FileExistsError
                else:
                    runtimelog = subprocess.run(["py" if os.name == 'nt' else "python3", apppath, sstruct, todo, cwd])
            except FileExistsError:
                err = True

    if runtimelog is not None and runtimelog.returncode == 1:
        err = True

    if err == True:
        rand = random.randint(1, 3)
        if rand == 1:
            print("Cant Comprehend This.")
        elif rand == 2:
            print("Doesnt Ring a Bell.")
        elif rand == 3:
            print("Doesnt Work.")
