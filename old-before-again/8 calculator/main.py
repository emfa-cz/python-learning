operator = input("enter operator (+ - * /): ")
num1 = float(input("Enter number 1: "))
num2 = float(input("enter number 2: "))

if operator == "+":
    result = num1 + num2
    print(float(round(result, 3)))
elif operator == "-":
    result = num1 - num2
    print(float(round(result, 3)))
elif operator == "*":
    result = num1 * num2
    print(float(round(result, 3)))
elif operator == "/":
    result = num1 / num2
    print(float(round(result, 3)))
else:
    print("wrong input")
