import requests
import os
import sys

todo = sys.argv[1]
cwd = sys.argv[2]

if " -o " in todo:
    tofr = todo.split(" -o ")
    tofetch = tofr[0]
    if os.name == 'nt':
        if ":\\" in tofr[1]:
            tocr = tofr[1]
        else:
            tocr = os.path.join(cwd, tofr[1])
    else:
        if tofr[1].startswith("C:\\"):
            tocr = (tofr[1])[3:].replace("\\", "/")
        else:
            tocr = os.path.join(cwd, tofr[1])
else:
    tofetch = todo
    last = todo.rsplit("/", 1)[-1]
    if "." in last:
        tocr = os.path.join(cwd, last)
    else:
        tocr = os.path.join(cwd, f"{last}.html")


try:
    html = requests.get(tofetch).text
    with open(tocr, "w") as https:
        https.write(html)
    print("Injection is Successfull")
except Exception as e:
    print(e)