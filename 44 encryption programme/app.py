import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
charList = []
for char in chars:
    charList.append(char)
chars = charList

key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

# encrypt

plain = input("enter message to be encrypted: ")
cipher = ""

for letter in plain:
    index = chars.index(letter)
    cipher += key[index]

print(f"original message: {plain}")
print(f"ecnrypted message: {cipher}")


# decrypt

cipher = input("enter message to be encrypted: ")
plain = ""

for letter in plain:
    index = key.index(letter)
    plain += key[index]

print(f"ecnrypted message: {cipher}")
print(f"original message: {plain}")
