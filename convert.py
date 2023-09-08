import glob, os

for x in glob.glob("slides/*.pdf"):
    os.system(f"pdftoppm {x} {x} -png")
