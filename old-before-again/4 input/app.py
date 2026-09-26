# input() = prompt aby user napsal data, vrati data jako str

name = input("jmeno: ")
age = input("vek: ")
age = int(age)
pristi_vek = age + 1
age2 = int(input("vek pro overeni: "))
minuly_age = age2 - 1

print(f"krasny den {name}, tvuj vek je {age} a za rok ti bude {pristi_vek} a minule ti bylo {minuly_age}")




