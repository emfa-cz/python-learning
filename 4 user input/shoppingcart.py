item = input("what would you like to buy: ")
price = float(input("what is the price: "))
qty = int(input("how many: "))

total = price * qty

print(f"the total of {qty}x {item}(s) is: {total} EUR")