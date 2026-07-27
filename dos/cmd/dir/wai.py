import sys
import os

cwd = sys.argv[3]
if os.name == 'nt':
    print(cwd)
else:
    ncwd = "C" + cwd.replace("/", "\\")
    print(ncwd)