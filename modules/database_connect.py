import mysql.connector
from . import table_print

# Connects to Database 
def connectDb():
    mydb = mysql.connector.connect(
            host="localhost",
            user="cs4430",
            password="cs4430",
            database="northwind",
            auth_plugin="mysql_native_password"
    )

    return mydb

#Gets information from a custormer
def getCustomerInfo(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Get Info of a customer given an ID
    sql = "SELECT CustomerID, CompanyName, ContactName, ContactTitle, Address, Country, Phone from customers WHERE CustomerID = %s"
    val = (ID, )

    #Get information and present it to the user
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if (not result):
        return 1
    else:
        table_print.printTable(result, ["CustomerID", "CompanyName", "ContactName", "ContactTitle", "Address", "Country", "Phone"])
        return 0

#Gets information from an employee
def getEmployeeInfo(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Get info of an employee given an ID
    sql = "SELECT EmployeeID, LastName, FirstName, Country, HomePhone FROM employees WHERE EmployeeID = %s"
    val = (ID, )

    #Get information and present it to the user
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if (not result):
        return 1
    else:
        table_print.printTable(result, ["EmployeeID", "LastName", "FirstName", "Country", "HomePhone"])
        return 0

#Gets information from a shipper
def getShipperInfo(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Get info of a shipper given an ID
    sql = "SELECT ShipperID, CompanyName, Phone FROM shippers WHERE ShipperID = %s"
    val = (ID, )

    #Get information and present it to the user
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if (not result):
        return 1
    else:
        table_print.printTable(result, ["ShipperID", "CompanyName", "Phone"])
        return 0

#Gets information from a product
def getProductInfo(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Get Info of product given an ID
    sql = "SELECT ProductID, ProductName, UnitsInStock from products WHERE ProductId = %s"
    val = (ID, )

    #Get information and present it to the user
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if (not result):
        return 1
    else:
        table_print.printTable(result, ["ProductID", "ProductName", "UnitsInStock"])
        return 0

#Gets information from an order
def getOrderInfo(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Get Info of order given an ID
    sql = "SELECT OrderID, CustomerID, OrderDate, ShippedDate FROM orders WHERE OrderID = %s"
    val = (ID, )

    #Get information and present it to the user
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if (not result):
        return 1
    else:
        table_print.printTable(result, ["OrderID", "CustomerID", "OrderDate", "ShippedDate"])
        # If it hasn't been shipped yet...
        if(not result[0][3]):
            return 0
        return 2

#1th Option. Inserts a new customer into 'customers'
def addCustomer(db, ID, info):
    cursor = db.cursor()

    #Prepare SQL -- Inserts a new customer into the table 'customers'
    sql = "INSERT INTO customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City," \
        "Region, PostalCode, Country, Phone, Fax) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (ID, info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9])

    #Execute and commit to the database
    cursor.execute(sql, val)
    db.commit()

    #Prepare presentation to the user
    print("\n\nDB:", cursor.rowcount, "record(s) inserted")
    print("DB: Successfully added customer into customers")

    return 0

#2th Option. Inserts a new order into 'order' and products into 'order_details'
def addOrder(db, order, products):
    cursor = db.cursor()

    #Prepare SQL -- Get Postal Code for Customer of this order
    sql = "SELECT PostalCode FROM customers WHERE CustomerID = %s"
    val = (order[0], )

    #Execute and get value
    cursor.execute(sql, val)
    postal = cursor.fetchall()

    #Prepare SQL -- Inserts a new order into the table 'orders'
    sql = "INSERT INTO orders (CustomerID, EmployeeID, OrderDate, ShipVia, Freight, ShipName, ShipAddress," \
        "ShipCity, ShipRegion, ShipPostalCode, ShipCountry) VALUES (%s, %s, CURRENT_TIMESTAMP(), %s, %s," \
        "%s, %s, %s, %s, %s, %s)"
    val = (order[0], order[1], order[2], order[3], order[4], order[5], order[6], order[7], postal[0][0], order[8])

    #Execute to the database
    cursor.execute(sql, val)

    #Prepare SQL -- Get newly inserted order
    sql = "SELECT MAX(OrderID) FROM orders"

    #Execute and get value
    cursor.execute(sql)
    orderid = cursor.fetchall()

    #For each product to add...
    for p in products:
        #Prepare SQL -- Inserts a new order/product into 'order_details'
        sql = "INSERT INTO order_details (OrderID, ProductID) VALUES (%s, %s)"
        val = (orderid[0][0], p)

        #Execute to the database
        cursor.execute(sql, val)


    #Commit all changes to the database
    db.commit()

    #Prepare presentation to the user
    print("DB: Successfully added order to order and order_details")

    return 0

#3th Option. Removes an order from orders & order_details. Updates 'UnitsOnOrder'
def removeOrder(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Delete ALL order_details from order_details that have ID
    sql = "DELETE FROM order_details WHERE OrderID = %s"
    val = (ID, )

    cursor.execute(sql, val)
    
    #Preate SQL -- Delete order ID from orders
    sql = "DELETE FROM orders WHERE OrderID = %s"
    val = (ID, )

    cursor.execute(sql, val)

    #Prepare SQL -- Update 'UnitsOnOrder' from products?

    #Commit to the database
    db.commit()

    #Prepare presentation to the user
    print("\n\nDB:", cursor.rowcount, "record(s) updated")
    print("DB: Successfully removed order from orders and order_details")

    return 0

#4th Option. Ships an order that hasn't been shipped

def shipOrder(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Updates 'ShippedDate' from 'NULL' to Current Date
    sql = "UPDATE orders SET ShippedDate = CURRENT_TIMESTAMP() WHERE OrderID = %s"
    val = (ID, )

    cursor.execute(sql, val)

    #Commit to the database
    db.commit()

    #Prepare presentation to the user
    print("\n\nDB:", cursor.rowcount, "record(s) updated")
    print("DB: Successfully updated ShippedDate for the order:")

    return 0

#5th Option. Gets pending orders
def pending(db):
    cursor = db.cursor()

    #Prepare SQL -- Get Info of order without a shipped date
    sql = "SELECT DISTINCT OrderID, OrderDate, CompanyName, ContactName, Country, Phone" \
     + " FROM customers NATURAL JOIN (SELECT OrderID, CustomerID, OrderDate" \
     + " FROM orders WHERE ShippedDate IS NULL) R1";

    cursor.execute(sql)
    
    #Prepare presentation to the user
    result = cursor.fetchall()
    print("\n\nDB: Printing all orders pending to be shipped...\n\n")
    table_print.printTable(result, ["OrderId", "OrderDate", "CompanyName", "ContactName", "Country", "Phone"])
    
    return 0

#6th Option. Restocks a product
def restock(db, ID, num):
    cursor = db.cursor()

    #Prepare SQL -- Adds 'num' to 'UnitsInStock' of 'ID' given product
    sql = "UPDATE products SET UnitsInStock = UnitsInStock + %s WHERE ProductId = %s"
    val = (num, ID)

    cursor.execute(sql, val)
    
    #Commit to the database changes
    db.commit()

    #Prepare presentation to the user
    print("\n\nDB:", cursor.rowcount, "record(s) updated")
    print("DB: Successfully updated Units In Stock for the product:")
    
    return 0

# This is to be used as an imported module
if __name__ == "__main__":
    print("Please do not run this independently. Contact programmer")
