from modules import *

def main():
    mydb = database_connect.connectDb()

    #Program runs until exit
    while(True):
        #Gets input and checks that it is valid
        option = menu()
        if (checkNum(option)):
            continue

        if (switch_options(int(option), mydb)):
            print("\nPlease provide a number between 1 - 7")
            continue

def checkNum(num):
    if (not num.isdigit()):
        print("\nPlease give a proper number input.")
        return 1
    
    return 0

#Option selects
def switch_options(number, mydb):
    if (number == 1):
        return 0
    elif (number == 2):
        return 0
    elif (number == 3):
        return 0
    elif (number == 4):
        return 0
    elif (number == 5):
        database_connect.pending(mydb)
        return 0

    elif (number == 6):
        print("\n\nPlease provide the ID or the Name of the product you wish to restock: ")
        ID = input()
        if (not database_connect.getProductInfo(mydb, ID)):
            print("\nHow much do you wish to add to the product above? (Between 0 - 100)")
            toAdd = input()
            if (checkNum(toAdd)):
                return

            #This is to just add some at time
            if (int(toAdd) < 0 or int(toAdd) > 100):
                print("\nPlease provide a valid number between 0 - 100")
                return

            database_connect.restock(mydb, ID, toAdd)
            database_connect.getProductInfo(mydb, ID)
        return 0

    elif (number == 7):
        print("\nThank you for using my app. Have a good day :).\n")
        exit(0)

    else:
        return 1
        

#Prints menu and gets user input
def menu():
    print("\n1. add customer"   \
    + "\n2. add an order"       \
    + "\n3. remover an order"   \
    + "\n4. ship an order"      \
    + "\n5. print pending orders with customer information" \
    + "\n6. restock products" \
    + "\n7. exit" )

    return input()


if __name__ == "__main__":
    main()
