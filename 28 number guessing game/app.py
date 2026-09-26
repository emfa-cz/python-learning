import random

low = 1
high = 1000
answer = random.randint(low, high)
guesses = 0
isRun = True

print("python num guess game")
print(f"select num between {low} and {high}")


while isRun:

    guess = input("Enter guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("wroooong")
        elif guess < answer:
            print("woo low ")
        elif guess > answer:
            print("too hi")
        else:
            print(f"ding ding ding correct was {answer}")
            print(f"num of guesses: {guesses}")
            isRun = False
    else:
        print("invalid guess")