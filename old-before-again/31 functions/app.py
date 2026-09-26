def hb(name, age):
    print(f"happy bday {name}")
    print(f"you are {age} yrs old")
    print(f"happy bday {name}")

hb("emfa", 20)

print("-----------------")

def invoice(uname, amt, date):
    print(f"hello {uname}")
    print(f"your bill of {amt:.2f} is due : {date}")

invoice("emfa", 200.6713, "24/2/26")


def add(x, y):
    z = x + y
    return z

def subt(x, y):
    z = x - y
    return z

def mply(x, y):
    z = x * y
    return z

def dvde(x, y):
    z = x / y
    return z

print(add(1, 2))


def cteName(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

fullName = cteName("em", "fa")

print(fullName)