from datetime import datetime,timedelta,date,time
import time
import sqlite3

def displaySingleDate():
    # Connect to the SQLite database file
    conn = sqlite3.connect('/home/neal/oopTemp/oopTemp.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data WHERE strftime('%d',date) = ?",[dateValue])
    
    rows = cursor.fetchall()

    # Iterate over the rows and print the data
    for row in rows:
       id, date, piTemp, piHumidity, webTemp, webOvercast = row
       print(f"ID: {id}, Date: {date}, Temperature: {piTemp}, Humidity: {piHumidity}, Web Temp: {webTemp}, Cloud Info: {webOvercast}")

def deleteSingleItem():
    # Connect to the SQLite database file
    conn = sqlite3.connect('/home/neal/oopTemp/oopTemp.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data WHERE strftime('%d',date) = ? and ID = ?",[dateValue,value])        
    
    rows = cursor.fetchall()        

    # Iterate over the rows and print the data
    for row in rows:
       id, date, piTemp, piHumidity, webTemp, webOvercast = row
       print(f"ID: {id}, Date: {date}, Temperature: {piTemp}, Humidity: {piHumidity}, Web Temp: {webTemp}, Cloud Info: {webOvercast}")
    
    # Check that we found only a single match before deleting this
    # particular row
    if (len(rows) != 1):
      print("Item not found in this date range, check input and try again.")
      # Close the cursor and connection
      cursor.close()
      conn.close()
      quit()    

    cursor.execute("DELETE FROM data WHERE strftime('%d',date) = ? and ID = ?",[dateValue,value])
    
    #Commit your changes in the database
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

dateValue = input("Enter date which contains the item you wish to remove DD):\n")
if (len(dateValue) == 1):
    dateValue = '0' + dateValue

print('Searching for\n\n',dateValue)    
displaySingleDate()

value = input("Enter item number to remove:\n\n")
deleteSingleItem()

print('Item Deleted')
