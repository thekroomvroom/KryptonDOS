import os
import sys

todo = sys.argv[1]
cwd = sys.argv[2]

# IP Setup
rdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
adir = os.path.join(os.path.dirname(rdir), "app")

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
        # Integrity Check

        rcr = os.path.realpath(cr)
        rrdir = os.path.realpath(rdir)
        radir = os.path.realpath(adir)

        if rcr.startswith(rrdir + os.sep) or rcr.startswith(radir + os.sep) or rcr == rrdir or rcr == radir:
            print(f"new: {rcr if os.name == 'nt' else "C:" + rcr.replace("/", "\\")}; Operation not Permitted.")

        else:
            try:
                os.mkdir(rcr)
                print("Success.")
            except Exception as e:
                print(e)
