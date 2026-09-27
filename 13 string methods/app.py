name = input("enter your full name: ")

result = len(name)
result = name.find("e")
result = name.rfind("a")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()

print(result) 


uname = input("enter your username: ")
if len(uname) > 13 or not uname.find(" ") == -1 or uname.isalpha() == False:
    print("wrong input")
else:
    print(f"your username is: {uname}")