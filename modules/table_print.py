from beautifultable import BeautifulTable

#Prints in a pretty, table fashion a query result
def printTable(query, headers):
    table = BeautifulTable(max_width=160)
    table.set_style(BeautifulTable.STYLE_GRID)
    table.column_headers = headers

    for row in query:
        table.append_row(row)

    print(table)

# This is to be used as an imported module
if __name__ == "__main__":
    print("Please do not run this independently. Contact programmer")

