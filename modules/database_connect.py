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

#Gets information from a product
def getProductInfo(db, ID):
    cursor = db.cursor()

    #Prepare SQL -- Get Info of product given an ID
    sql = "SELECT ProductID, ProductName, UnitsInStock from products WHERE ProductId = %s"
    val = (ID, )

    cursor.execute(sql, val)

    #Prepare presentation to the user
    result = cursor.fetchall()
    if (not result):
        print("\n\n------- No product with given ID was found. --------\n\n")
        return 1
    else:
        table_print.printTable(result, ["ProductID", "ProductName", "UnitsInStock"])
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
    print("\n\n", cursor.rowcount, "record(s) updated")
    print("Successfully updated Units In Stock for the product:")
    
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
    print("\n\nPrinting all orders pending to be shipped...\n\n")
    table_print.printTable(result, ["OrderId", "OrderDate", "CompanyName", "ContactName", "Country", "Phone"])
    
    return 0



# This is to be used as an imported module
if __name__ == "__main__":
    print("Please do not run this independently. Contact programmer")
