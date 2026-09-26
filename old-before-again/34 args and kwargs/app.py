def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))



def displayName(*args):
    for arg in args:
        print(arg, end=" ")

displayName("Em", "Fa")

print()


# kwargs
def printAddr(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printAddr(street="123 fake street", city="usti nad labem", state="cz", zip="12345")



def ShippingLabel(*args, **kwargs):
    pass

ShippingLabel()