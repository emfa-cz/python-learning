# === print a komentare ===


print("test")
print("toto j etest teto skvele klavesnice ale nenavidim ji")
# toto je test pyssthon





# === variables ===

# Strings
name = "Petr Pichal"
emil = "petrlik.honzik@gmail.com"

# Integers
age = 10

# Float
price = 67.42

# Boolean
rad_nergy = False

print(name) # obycejne print var
print(f"jemnuji se {name} a je mi {age} prodavam novy ipon za {price} plsky zavolej mi na {emil} ")

if rad_nergy:
    print("nesu novinky miluju nergy moc mocinky")
else:
    print("sel jsem do sratnetu na maj a najednou se setmelo")






# Typecasting = proces prevedeni jednoho data type na jiny

name = "Katerina Prepazkova"
age = 67
kc_ucet = 8.12
potrebuju_chcat = True

print (type(name)) # print data type varu

# konverze data type
age = str(age)
print(type(age))

age += "8"
print(f"dostali jsme {age} protoze pracujeme s data type string")






