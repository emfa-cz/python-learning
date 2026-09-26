capitals = {"USA": "Washington DC",
            "india": "new delhi",
            "china": "beijing",
            "russia": "moscow"
            }

#print(dir(capitals))

print(capitals.get("USA"))

if capitals.get("russia"):
    print("exists")
else:
    print("dont exists")

capitals.update({"germany": "berlin"})

#capitals.popitem()

#capitals.clear()

keys = capitals.keys()

#for key in capitals.keys():
#    print(key)



#print(keys)

#values = capitals.values()
#print(values)

#items = capitals.items()
#print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")