class employee:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    def getInfo(self):
        return f"{self.name} = {self.pos}"



    @staticmethod
    def isValPos(pos):
        valPoss = ["manager", "cashier", "cook", "janitor"]
        return pos in valPoss

employee1 = employee("eugene", "manager")
employee2 = employee("squidward", "cashier")
employee3 = employee("spongebob", "cook")

print(employee.isValPos("rocket scierntist"))
print(employee1.getInfo())