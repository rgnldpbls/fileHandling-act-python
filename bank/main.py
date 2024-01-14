def openAcc():
    while True:
        actName = input("Enter Account Name: ")
        if len(actName) <= 30:
            break
        else:
            print("Please input at most 30 characters\n")

    while True:
        pinNum = input("Enter PIN: ")
        if pinNum.isnumeric():
            if len(pinNum) == 4:
                break
            else:
                print("Please input only 4 Number!\n")
        else:
            print("Please input only Number!\n")

    while True:
        try:
            initBal = int(input("Enter Initial Balance:P "))
            break
        except ValueError:
            print("Please input only Number!\n")

    f.write(f"{actNum},{actName},{pinNum},{str(initBal)}")
    print(f"Account Number {actNum} Created Successfully!")

x = True
while x:
    f = open("Accounts.txt", "a")
    while True:
        actNum = input("Enter Account Number: ")
        if actNum.isnumeric():
            if len(actNum) == 5:
                break
            else:
                print("Please input only 5 Number!\n")
        else:
            print("Please input only Number!\n")

    found = False
    with open("Accounts.txt", "r") as file:
        for line in file:
            accNo, accName, pinNo, initBalance = line.strip().split(",")
            if actNum == accNo:
                found = True

    if found:
        print("Account Already exist! Please Try Again...")
    else:
        openAcc()

    while True:
        ans = input("\nEnter more?[Y/N]: ").upper()
        if ans == "Y":
            print()
            break
        elif ans == "N":
            f.close()
            x = False
            break
        else:
            print("Invalid Input\nTry Again!\n")

def balInq():
    with open("Accounts.txt", "r") as file:
        for line in file:
            accNo, accName, pinNo, initBalance = line.strip().split(",")
            print(f"\nYour Balance is P{initBalance}.\n")

def depAcc():
    updAcc = []
    with open("Accounts.txt", "r") as file:
        for line in file:
            accNo, accName, pinNo, initBalance = line.strip().split(",")
            while True:
                try:
                    dep = int(input("\nEnter amount you want to deposit: "))
                    break
                except ValueError:
                    print("Please input only Number!\n")

            newBal = dep + int(initBalance)
            updAcc.append(f"{accNo},{accName},{pinNo},{str(newBal)}")
            with open("Accounts.txt", "w") as file:
                file.writelines(updAcc)
            file.close()
            print("Deposited Successfully!")

def withdAcc():
    updAcc = []
    with open("Accounts.txt", "r") as file:
        for line in file:
            accNo, accName, pinNo, initBalance = line.strip().split(",")
            while True:
                try:
                    withd = int(input("\nEnter amount you want to withdraw: "))
                    if withd < int(initBalance):
                        break
                    else:
                        print("Insufficient Balance! Please Try Again...")
                except ValueError:
                    print("Please input only Number!\n")
            newBal = int(initBalance) - withd
            updAcc.append(f"{accNo},{accName},{pinNo},{str(newBal)}")
            with open("Accounts.txt", "w") as file:
                file.writelines(updAcc)
            file.close()
            print("Withdraw Successfully!")

def menu():
    while True:
        pinNum = input("Enter PIN: ")
        if pinNum.isnumeric():
            if len(pinNum) == 4:
                break
            else:
                print("Please input only 4 Number!\n")
        else:
            print("Please input only Number!\n")

    with open("Accounts.txt", "r") as file:
        for line in file:
            accNo, accName, pinNo, initBalance = line.strip().split(",")
            if pinNum == pinNo:
                while True:
                    print("\nWelcome to PUP On-Line Banking Systems")
                    print("\n1. Balance Inquiry")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Cancel")
                    try:
                        choice = int(input("Press the desired transaction: "))
                        if choice == 1:
                            balInq()
                        elif choice == 2:
                            depAcc()
                        elif choice == 3:
                            withdAcc()
                        elif choice == 4:
                            print("Program Termination!")
                            exit(0)
                        else:
                            print("Invalid Input! Please Try Again...")
                    except ValueError:
                        print("Invalid Input! Please Try Again...")
            else:
                print("Invalid Pin! Program Termination...")
                exit(0)

y = True
attempt = 0
while y:
    while True:
        actNum = input("\nEnter Account Number: ")
        if actNum.isnumeric():
            if len(actNum) == 5:
                break
            else:
                print("Please input only 5 Number!\n")
        else:
            print("Please input only Number!\n")

    found = False
    with open("Accounts.txt", "r") as file:
        for line in file:
            accNo, accName, pinNo, initBalance = line.strip().split(",")
            if actNum == accNo:
                found = True
    if found:
        y = False
        menu()
    else:
        print("Sorry the Account doesn't exist!")
        attempt += 1
        if attempt > 2:
            y = False
            print("Program Termination!")
            exit(0)
