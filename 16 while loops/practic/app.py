sel = ""
finalPrice = 0
prc = {
    1: 12.00,
    2: 24.99,
    3: 15.49
}

print("---- SHOPPING CART ----")
print("[q] quit")
print("[1] bread | 12.00")
print("[2] chocolate | 24.99")
print("[3] milk | 15.49")
print("------------------------")
sel = input("choose: ")

while not sel == "q":
    if sel.isdigit() == True:
        if not sel == "q" and (not sel.isdigit() == True or sel <1 or sel >3 or sel.isdecimal == True):
            print("enter valid..")
        elif not sel == "q" and sel.isdigit() and sel >= 1 and sel <= 3 and sel.isdecimal == False:
            sel = int(sel)
            print(f"selected number {sel}.")
            howMany = int(input("how many: "))
            if not howMany.isdigit() or howMany.isdecimal() or howMany <1:
                print("wrong input")
            else:
                finalPrice = finalPrice + howMany * prc[sel]
    else:
        print("wrong input")

if sel == "q":
    print("----- checkout -----")
    print(f"the total is: {finalPrice}")
    print("cash or card?")
    payMeth = str(input("choose: "))
    payMeth = payMeth.lower()
    while not payMeth == "cash" and not payMeth == "card":
        print("invalid input..")
        print("cash or card?")
        payMeth = str(input("choose: "))
        payMeth = payMeth.lower()


# fix all later