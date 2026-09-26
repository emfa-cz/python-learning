princ = 0
rate = 0
time = 0

while princ <= 0:
    princ = int(input("enter your principle: "))
    if princ <= 0:
        print("wrong amt")

while rate <= 0:
    rate = int(input("enter your rate: "))
    if rate <= 0:
        print("wrong amt")
        
while time <= 0:
    time = int(input("enter your time yrs: "))
    if time <= 0:
        print("wrong amt")

total = princ * pow((1 + rate / 100), time)

print(f"balance after {time} years: ${total:.2f}")