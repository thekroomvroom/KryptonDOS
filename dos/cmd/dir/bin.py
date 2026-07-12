import sys
import os

todo = sys.argv[1]
cwd = sys.argv[2]

if '/' in todo:
    sys.exit(1)
else:
    pt = os.path.realpath(todo) if os.name == 'nt' else os.path.realpath(todo.replace("\\", "/"))
    with open(pt, "r") as f:
        print(f.read())