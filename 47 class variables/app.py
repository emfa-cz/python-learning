class student:
    classYr = 2024
    amtStuds = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.amtStuds += 1

stud1 = student("em", 30)
stud2 = student("fa", 35)
stud3 = student("faem", 123)

print(stud1.name)
print(stud1.classYr)
print(student.amtStuds)