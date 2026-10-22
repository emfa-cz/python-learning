
try:
    num = int(input("enter a number: "))
    print(1 / num)
except ZeroDivisionError:
    print("no div by 0")
except ValueError:
    print("enter only nm")
except Exception:
    print("something went wrong")
finally:
    print("do some cleanup")