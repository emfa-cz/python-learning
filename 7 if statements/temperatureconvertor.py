print("---- TEMPERATURE CONVERSION PROGRAMME -----")
print("Choose one:\n[1] C to F\n[2] F to C")
mode = int(input("Your selection: "))

if mode == 1:
    print("[SELECTED MODE 1]")
    unitFinal = "F"
    ces = float(input("Enter Celsius amount: "))
    result = ces * 9/5 + 32
elif mode == 2:
    print("[SELECTED MODE 2]")
    unitFinal = "C"
    fah = float(input("Enter Farenheit amount: "))
    result = (fah - 32) * 5/9
else:
    print("wrong input run the program again because i forgot how to make while loops")


if mode == 1 or 2 and result == True:
    print(f"The result is: {result}{unitFinal}")