import sys
import os
import shutil


rdir = os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
adir = os.path.realpath(os.path.join(os.path.dirname(rdir), "app"))


todo = sys.argv[1]
dirat = sys.argv[2]

todp = todo.split(" ")
amt = len(todp)

if int(amt) % 2 != 0:
    sys.exit(1)
else:
    for i in range(1, int(amt) + 1, 2):
        dpls = todp[i - 1]
        nnls = todp[i]
        cwd = dirat

        if os.name == 'nt':
            if ":\\" in dpls:
                dp = os.path.realpath(dpls)
            else:
                dp = os.path.abspath(dpls)
            if ":\\" in nnls:
                nn = os.path.realpath(nnls)
            else:
                nn = os.path.abspath(nnls)
        else:
            if dpls.startswith("C:\\"):
                dp = dpls[2:].replace("\\", "/")
            else:
                dp = os.path.abspath(dpls)
            if nnls.startswith("C:\\"):
                nn = os.path.realpath(nnls)
            else:
                nn = os.path.abspath(nnls)

        if dp.startswith(rdir + os.sep) or dp.startswith(adir + os.sep) or dp == rdir or dp == adir:
            display_path = dp if os.name == 'nt' else "C:" + dp.replace("/", "\\")
            print(f"dupe source: {display_path}; Operation Refused")
            

        elif nn.startswith(rdir + os.sep) or nn.startswith(adir + os.sep) or nn == rdir or nn == adir:
                    display_path = nn if os.name == 'nt' else "C:" + dp.replace("/", "\\")
                    print(f"dupe dest: {display_path}; Operation Refused")
        else:
            try:
                if os.path.isfile(dp):
                    shutil.copyfile(dp, nn)
                    print("Operation Success.")
                elif os.path.isdir(dp):
                    shutil.copytree(dp, nn)
                    print("Operation Success.")
                else:
                    print("Specified File or Directory Does Not Exist.")
            except Exception as e:
                print(e)