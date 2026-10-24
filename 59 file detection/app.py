import os

filePath = "./test.txt"

if os.path.exists(filePath):
    print(f"the location {filePath} exists")
else:
    print("that location doesnt exist")

if os.path.isfile(filePath):
    print(f"it is a file")
else:
    print("it is a dir")