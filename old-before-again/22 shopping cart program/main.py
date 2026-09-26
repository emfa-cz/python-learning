foods = []
prices = []
total = 0

while True:
    food = input("enter food to buy (o to ok): ")
    if food.lower() == "o":
        break
    else:
        price = float(input(f"enter price of {food}: "))
        foods.append(food)
        prices.append(price)

print("---- CART ----")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"total: {total}")