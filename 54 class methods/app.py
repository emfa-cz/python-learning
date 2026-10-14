class student:
    count = 0
    ttl = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.ttl += gpa

# instance meth odd
    def getInfo(self):
        return f"{self.name} {self.gpa}"

        
    @classmethod
    def getCount(cls):
        return f"total # of students: {cls.count}"

    @classmethod
    def getAvgGpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.ttl / cls.count:.2f}"

student1 = student("spongebob", "3.2")

student2 = student("patrik", "1.4")

student3 = student("sandy", "4.7 ")


print(student.getCount())
print(student.getAvgGpa())

