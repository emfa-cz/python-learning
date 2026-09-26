quests = ("how many elements are in the periodic table: ",
          "which animal lays the largest eggs: ",
          "what is the most abundant gas in earths atmosphere: ",
          "hoe many bones are in tyhe human body (boner != a bone): ",
          "which planet in the solar system is the hottest (not your mom): ")

opts = (("A. 67", "B. 117", "C. 118", "D. 119"),
        ("A. whale", "B. croc", "C. elephant", "D. osterreich"),
        ("A. nitrogen", "B. oxygen", "C. carbon dioxide", "D. hydrogen"),
        ("A. 206", "B. 207", "C. 208", "D. 209"),
        ("A. mercury", "B. venus", "C. earth", "D. mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
questNum = 0

for quest in quests:
    print(f"---------------\n{quest}")
    for opt in opts[questNum]:
        print(opt)

    guess = input("Enter option: ").upper()
    guesses.append(guess)
    if guess == answers[questNum]:
        score += 1
        print("correct")
    else:
        print("wrooong")
        print(f"{answers[questNum]} is correct")

    questNum += 1

print("RESULT: \n")
print("answers: ", end="")
for answer in answer:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(quests) * 100)