temp = 60
isRaining = False

if temp > 35 or temp < 0 or isRaining == True:
    print("bad weather")
else:
    print("ok weather")




temp = 29
isRaining = True

if temp >= 28 and isRaining == False:
    print("pocasi na koupani")
else:
    print("neni pocasi na koupani")




temp = 45
isRaining = False

if temp >= 40 and not isRaining:
    print("to je teda vedro")
else:
    print("ok weather")