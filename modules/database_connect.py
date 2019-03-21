import mysql.connector
from beautifultable import BeautifulTable

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

#Prints in a pretty, table fashion a query result
def printTable(query, headers):
    table = BeautifulTable(max_width=160)
    table.set_style(BeautifulTable.STYLE_GRID)
    table.column_headers = headers

    for row in query:
        table.append_row(row)

    print(table)


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
    printTable(result, ["OrderId", "OrderDate", "CompanyName", "ContactName", "Country", "Phone"])
    
    return 0



# This is to be used as an imported module
if __name__ == "__main__":
    print("Please do not run this independently. Contact programmer")
