word = "APPLE"

letter = input("guess a letter in the secret word: ")

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} not found")