def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3))



#kwargs
def addr(**kwargs):
    for value in kwargs.values():
        print(value)

addr(
    street="terst",
    city="usti nad labem",
    country="cz"
)