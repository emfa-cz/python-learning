age = int(input("enter your age: "))

if age >100:
    print("too big")
elif age < 1:
    print("enter at least 1")
elif age >= 18:
    print("18 or above")
else:
    print("17 or lower")