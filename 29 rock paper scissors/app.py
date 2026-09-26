import random
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options) 
running = True

while running:



while player not in options:
    player = input("enter a choice (rock paper scissors): ")



print(f"player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("tie")
elif player == "rock" and computer == "scissors":
    print("player win")
elif player == "paper" and computer == "rock":
    print("player win")
elif player == "scissors" and computer == "paper":
    print("player win")
else:
    print("player lose")