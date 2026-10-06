def dayWeek(day):
    match day:
        case 1:
            return "it is mobnday"
        case 2:
            return "it is tuesday"
        case _:
            return "not valid"

print(dayWeek("test"))
print(dayWeek(2))