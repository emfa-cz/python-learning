import random

number = random.randint(1, 6)

print(number)

number = random.random()
print(number)

options = ("rock", "paper", "scissors")
opt = random.choice(options)
print(opt)