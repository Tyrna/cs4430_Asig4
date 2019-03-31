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
        print("\n\nPlease provide the ID of the customer you wish to add: ")
        ID = input()
        if (not ID or len(ID) > 5):
            print("\nInvalid Input. Please provide a proper CustomerID (Max. 5 characters)")
            return 0
        if (database_connect.getCustomerInfo(mydb, ID)):
            info = get_customer_info()
            if (info):
                if (not database_connect.addCustomer(mydb, ID, info)):
                    database_connect.getCustomerInfo(mydb, ID)
                    print("\nCustomer added to 'customers'.")
                    return 0
        else:
            print("\n\nA customer with this ID already exists, info above")
                
        return 1
    elif (number == 2):
        return 0
    elif (number == 3):
        print("\n\nPlease provide the ID of the order you wish to remove: ")
        ID = input()
        ret = database_connect.getOrderInfo(mydb, ID)
        if(not ret or ret == 2):
            print("\nAre you sure you wish to remove the above order? Y/N")
            confirm = input()
            if (confirm == 'Y' or confirm == 'y'):
                if (not database_connect.removeOrder(mydb, ID)):
                    database_connect.getOrderInfo(mydb, ID)
                    print("\nOrder removed from 'orders' and 'order_details'.")
                    return 0
        else:
            print("\n\n------- No order with given ID was found. -------\n\n")

        return 0
    elif (number == 4):
        #Id of the Order
        print("\n\nPlease provide the ID of the order you wish to ship: ")
        ID = input()
        ret = database_connect.getOrderInfo(mydb, ID)
        if (ret == 2):
            print("\n\nOrder has already been shipped!")
            return 0

        if (not ret):
            print("\nDo you wish to ship the above order today? Y/N")
            confirm = input()
            if (confirm == 'Y' or confirm == 'y'):
                if (not database_connect.shipOrder(mydb, ID)):
                    database_connect.getOrderInfo(mydb, ID)
                    print("\nAbove order has been shipped.")
                    return 0
            
            print("------- Order has not been shipped. -------")    

        else:
            print("\n\n------- No order with given ID was found. -------\n\n")

        return 0
    elif (number == 5):
        database_connect.pending(mydb)
        return 0

    elif (number == 6):
        print("\n\nPlease provide the ID of the product you wish to restock: ")
        ID = input()
        if (not database_connect.getProductInfo(mydb, ID)):
            print("\nHow much do you wish to add to the product above? (Between 0 - 100)")
            toAdd = input()
            if (checkNum(toAdd)):
                return

            #This is to just limit how many to add at a time
            if (int(toAdd) < 0 or int(toAdd) > 100):
                print("\nPlease provide a valid number between 0 - 100")
                return

            database_connect.restock(mydb, ID, toAdd)
            database_connect.getProductInfo(mydb, ID)
        else:
            print("\n\n------- No product with given ID was found. -------\n\n")

        return 0

    elif (number == 7):
        print("\nThank you for using my app. Have a good day :).\n")
        exit(0)

    else:
        return 1
        

#Obtains all the information needed to create a customer 
def get_customer_info():
    allInfo = []

    print("\nWhat is the 'Company Name'?")
    info = input()
    if (info and len(info)<40):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper company name (Max. 40 characters)") 
        return 0

    print("\nWhat is the 'Contact Name'?")
    info = input()
    if (info and len(info)<30):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper contact name (Max. 30 characters)") 
        return 0

    print("\nWhat is the 'Contact Title'?")
    info = input()
    if (info and len(info)<30):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper contact title (Max. 30 characters)") 
        return 0

    print("\nWhat is the 'Address'?")
    info = input()
    if (info and len(info)<30):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper address (Max. 60 characters)") 
        return 0

    print("\nWhat is the 'City'?")
    info = input()
    if (info and len(info)<15):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper city (Max. 15 characters)") 
        return 0

    print("\nWhat is the 'Region'?")
    info = input()
    if (info and len(info)<15):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper region (Max. 15 characters)") 
        return 0

    print("\nWhat is the 'Postal Code'?")
    info = input()
    if (info and len(info)<10):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper postal code (Max. 10 characters)") 
        return 0

    print("\nWhat is the 'Country'?")
    info = input()
    if (info and len(info)<15):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper country (Max. 15 characters)") 
        return 0 

    print("\nWhat is the 'Phone Number'?")
    info = input()
    if (info and len(info)<24):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper phone number (Max. 24 characters)") 
        return 0

    print("\nWhat is the 'Fax'?")
    info = input()
    if (info and len(info)<24):
        allInfo.append(info) 
    else:
        print("Invalid Input. Give a proper fax number (Max. 24 characters)") 
        return 0
        
    return allInfo

#Prints menu and gets user input
def menu():
    print("-" * 60  \
    + "\n1. add customer"   \
    + "\n2. add an order"       \
    + "\n3. remover an order"   \
    + "\n4. ship an order"      \
    + "\n5. print pending orders with customer information" \
    + "\n6. restock products" \
    + "\n7. exit" )

    return input()


if __name__ == "__main__":
    main()
