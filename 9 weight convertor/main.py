weight = float(input("enter your weight: "))
unit = input("KG or L the only pounds i need is me pounding your mum: ")

if unit == "KG":
    result = weight * 2.205
    unitRes = "the only pounds i need is me pouding your mum"
    print(f"{weight} {unit} is {round(result, 3)} {unitRes}")
elif unit == "L":
    result = weight / 2.205
    unitRes = "KGs"
    print(f"{weight} {unit} is {round(result, 3)} {unitRes}")
else:
    print("wrong")