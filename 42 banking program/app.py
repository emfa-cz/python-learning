def showBal(bal):
    print(f"your balance is: ${bal:.2f}")

def depos():
    amt = float(input("enter amout to be deposited: "))
    if amt == 0 or amt < 0:
        print("not valid amount")
        return 0
    else:
        return amt

def withdraw(bal):
    amt = float(input("enter amt to be withdrawn: "))
    if amt > bal:
        print("insufficient funds")
        return 0
    elif amt < 0:
        print("amout must be grater that 0")
        return 0
    else: 
        return amt
def main():

    bal = 0
    isRun = True


    while isRun:
        print("banking program")
        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")

        choice = input("enter choice (1-4): ")

        if choice == "1":
            showBal(bal)
        elif choice == "2":
            bal += depos()
        elif choice == "3":
            bal -= withdraw()
        elif choice == "4":
            isRun = False
        else:
            print("wrong input")


    print("bye")

if __name__ == '__main__':
    main()