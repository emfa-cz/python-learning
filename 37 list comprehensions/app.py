doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)



doubles2 = [x * 2 for x in range(1, 11)]
print(doubles2)

nums = [1, -2, 3, -4, 5, -6]
posNums = [num for num in nums if num >= 0]
print(posNums)