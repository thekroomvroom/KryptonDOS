import os
import sys

todo = sys.argv[1]
cwd = sys.argv[2]

if "/" in todo:
    print("File or Directory Specified Does Not Exist")

else:
    if " " in todo:
        crraw = todo.split(" ")
        amt = len(crraw)
    else:
        crraw = todo
        amt = 1

    for i in range(int(amt)):
        crls = crraw[int(i)]

        if os.name == 'nt':
            if ":\\" in kls:
                cr = crls
            else:
                cr = os.path.join(cwd, crls)
        else:
            if crls.startswith("C:\\"):
                cr = crls[2:].replace("\\", "/")
            else:
                cr = os.path.join(cwd, crls)

        try:
            os.mkdir(cr)
            print("Success.")
        except Exception as e:
            print(e)
