# Programming Activity No.6

f = open("Products.txt", "a")
x = True
while x:
    prodCode = input("Product Code: ")
    prodName = input("Product Name: ")
    while True:
        try:
            qty = int(input("Quantity: "))
            break
        except ValueError:
            print("Invalid Data Type, Try Again!\n")
    f.write(f"{prodCode},{prodName},{str(qty)}\n")
    print(f"Product {prodCode} Added Succesfully!")
    while True:
        ans = input("Enter more?[Y/N]: ").upper()
        if ans == "Y":
            print()
            break
        elif ans == "N":
            f.close()
            x = False
            break
        else:
            print("Invalid Input\nTry Again!\n")

def addRec():
    print()
    f = open("Products.txt", "a")
    prodCd = input("Product Code: ")
    found = False
    with open("Products.txt", "r") as file:
        for line in file:
            prodCode, prodName, qty = line.strip().split(",")
            if prodCode == prodCd:
                found = True
    if found:
        print(f"Product {prodCd} exist!")
    else:
        prodNm = input("Product Name: ")
        while True:
            try:
                prodqty = int(input("Quantity: "))
                break
            except ValueError:
                print("Invalid Data Type, Try Again!\n")
        f.write(f"{prodCd},{prodNm},{str(prodqty)}\n")
        print(f"Product {prodCd} Added Succesfully!")
        f.close()

def delRec():
    print()
    prdCd = input("Enter the product code you want to delete: ")
    del_Prod = []
    found = 0
    with open("Products.txt", "r") as file:
        for line in file:
            prodCode, prodName, qty = line.strip().split(",")
            if prodCode == prdCd:
                print(f"\nProduct Code: {prodCode}\nProduct Name: {prodName}\nQuantity: {qty}\n")
                while True:
                    ask = input("Are you sure you want to delete?[Y/N]: ").upper()
                    if ask == "Y":
                        found = 1
                        break
                    elif ask == "N":
                        found = 2
                        break
                    else:
                        print("Invalid Input\nTry Again!\n")
            else:
                del_Prod.append(line)
    file.close()

    if found == 1:
        with open("Products.txt", "w") as file:
            file.writelines(del_Prod)
        file.close()
        print(f"Product {prdCd} deleted Successfully!")
    elif found == 2:
        delRec()
    else:
        print(f"Product {prdCd} not found!")

def editRec():
    print()
    prdCd = input("Enter the product code you want to edit: ")
    upd_Prod = []
    found = 0
    with open("Products.txt", "r") as file:
        for line in file:
            prodCode, prodName, qty = line.strip().split(",")
            if prodCode == prdCd:
                print(f"\nProduct Code: {prodCode}\nProduct Name: {prodName}\nQuantity: {qty}\n")
                while True:
                    ask = input("Are you sure you want to edit?[Y/N]: ").upper()
                    if ask == "Y":
                        found = 1
                        new_cd = input("Enter the new Product Code: ")
                        new_name = input("Enter the new Product Name: ")
                        while True:
                            try:
                                new_qty = int(input("Enter the new Quantity: "))
                                break
                            except ValueError:
                                print("Invalid Data Type, Try Again!\n")
                        upd_Prod.append(f"{new_cd},{new_name},{new_qty}\n")
                        print(f"\nProduct Code: {new_cd}\nProduct Name: {new_name}\nQuantity: {new_qty}\n")
                        break
                    elif ask == "N":
                        found = 2
                        break
                    else:
                        print("Invalid Input\nTry Again!\n")
            else:
                upd_Prod.append(line)
    file.close()

    if found == 1:
        with open("Products.txt", "w") as file:
            file.writelines(upd_Prod)
        file.close()
        print(f"Product {prdCd} edited Successfully!")
    elif found == 2:
        print()
    else:
        print(f"Product {prdCd} not found!")

def transRec():
    print()
    prdCd = input("Enter the product code you want to edit: ")
    upd_Prod = []
    found = False
    with open("Products.txt", "r") as file:
        for line in file:
            prodCode, prodName, qty = line.strip().split(",")
            if prodCode == prdCd:
                print(f"Product Code: {prodCode}\nProduct Name: {prodName}\nQuantity: {qty}\n")
                while True:
                    transacCode = input("Enter transaction code[P/S]: ").upper()
                    if transacCode == "P":
                        while True:
                            try:
                                pqty = int(input("Purchased Quantity: "))
                                break
                            except ValueError:
                                print("Invalid Data Type, Try Again!\n")
                        new_qty = int(qty) + pqty
                        found = True
                        upd_Prod.append(f"{prodCode},{prodName},{str(new_qty)}\n")
                        print(f"\nProduct Code: {prodCode}\nProduct Name: {prodName}\nQuantity: {str(new_qty)}\n")
                        break
                    elif transacCode == "S":
                        while True:
                            try:
                                sqty = int(input("Sold Quantity: "))
                                if sqty > int(qty):
                                    print("Insufficient quantity, Try Again!\n")
                                else:
                                    break
                            except ValueError:
                                print("Invalid Data Type, Try Again!\n")
                        new_qty = int(qty) - sqty
                        found = True
                        upd_Prod.append(f"{prodCode},{prodName},{str(new_qty)}\n")
                        print(f"\nProduct Code: {prodCode}\nProduct Name: {prodName}\nQuantity: {str(qty)}\n")
                        break
                    else:
                        print("Invalid Input\nTry Again!\n")
            else:
                upd_Prod.append(line)
    file.close()

    if found:
        with open("Products.txt", "w") as file:
            file.writelines(upd_Prod)
        file.close()
        print(f"Product {prdCd} transaction successful!")
    else:
        print(f"Product {prdCd} not found!")


def mainMenu():
    y = True
    while y:
        print()
        print("[A] Add")
        print("[D] Delete")
        print("[E] Edit")
        print("[T] Transact")
        print("[X] Exit")
        choice = input("What do you want to do? ").upper()
        if choice == "A":
            addRec()
        elif choice == "D":
            delRec()
        elif choice == "E":
            editRec()
        elif choice == "T":
            transRec()
        elif choice == "X":
            with open("Products.txt", "r") as f:
                print("\nProduct List:")
                for line in f:
                    prodCode, prodName, qty = line.strip().split(",")
                    print(f"Product Code: {prodCode}\nProduct Name: {prodName}\nQuantity: {qty}\n")
            exit(0)
        else:
            print("Invalid Input\nTry Again!\n")

mainMenu()
