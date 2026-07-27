import sys
import os
import json
from datetime import datetime

todo = sys.argv[1]

def displaytime(tf):

    h = datetime.now().hour
    m = datetime.now().minute
    s = datetime.now().second
    
    if tf == 0:
        print(f"{int(int(h) / 2)}:{m}:{s} {datetime.now().strftime("%p")}")
    elif tf == 1:
        print(f"{h}:{m}:{s}")



if not todo == "":
    sys.exit(1)
else:
    timepath = os.path.join(os.path.dirname(os.path.dirname(sys.argv[4])), "sec", "tcf.json")
    with open(timepath, "r") as f:
        config = json.load(f)
    
    tformat = config["tf"]
    
    displaytime(tformat)