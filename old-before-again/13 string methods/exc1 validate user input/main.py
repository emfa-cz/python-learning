uname = input("Enter username: ")

if len(uname) > 10:
    print("too long didnt read")
elif uname.count(" ") >= 1:
    print("no spaces allow")
elif uname.isalpha() == False:
    print("no num allow")
else:
    print(f"ok {uname}")
