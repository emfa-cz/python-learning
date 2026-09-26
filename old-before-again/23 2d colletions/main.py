fruits = ["apple", "orange", "banana", "coconut"]
vegs =   ["celery", "carrots", "potatoes"]
meats =  ["chicken", "fih", "turkey"]

groceries = [fruits, vegs, meats]

#print(groceries[2][1])

#for collection in groceries:
#    print(collection)

for collection in groceries:
    for food in collection:
        print(food)