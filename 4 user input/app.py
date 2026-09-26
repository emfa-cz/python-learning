#input("what is your name: ")

name = input("what is your name: ")
age = input("what is your age: ")
price = float(input("what is the price: "))

age = int(age)
age = age + 1
price = price / 10

print(f"hello {name}")
print(f"you are {age} years old")
print(f"the price is {price}")