def hello(greet, tit, first, last):
    print(f"{greet} {tit} {first} {last}")

hello("hello", "ing. mudr. isc. mgr. bca. bc.", "katerina", "prepazkova")


def hello(greet, tit, first, last):
    print(f"{greet} {tit} {first} {last}")

hello(greet="hello", first="katerina", last="prepazkova", tit="ing. mudr. isc. mgr. bca. bc.")


for x in range(1, 11):
    print(x, end=" ")


def getPhone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phoneNum = getPhone(country=1, area=123, first=456, last=7890)

print(phoneNum)