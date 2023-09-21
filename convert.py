import glob, os
import sys
for x in sorted(glob.glob(f"slides/{sys.argv[1]}*.pdf")):
    print(x)
    os.system(f"pdftoppm {x} {x} -png")
