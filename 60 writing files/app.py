txtData = "i like pizza"
filePath = "output.txt"
filePath2 = "output2.txt"

emps = ["Eugene", "sqwd", "spgbb", "ptck"]

try:
    with open(file=filePath, mode="x") as file:
        file.write(txtData)
        print(f"text written")
except FileExistsError:
    print("that file exists")



    try:
        with open(file=filePath2, mode="w") as file:
            for emp in emps:
                file.write(f'{emp}\n')
            print(f"text written")
    except FileExistsError:
        print("that file exists")