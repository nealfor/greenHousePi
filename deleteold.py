from datetime import datetime,timedelta,date,time
import time
import sqlite3

def deleteOldItems():
    # Connect to the SQLite database file
    conn = sqlite3.connect('/home/neal/oopTemp/oopTemp.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data WHERE date < ?",[str(deleteDate)])
    
    rows = cursor.fetchall()

    # Iterate over the rows and print the data
    for row in rows:
       id, date, piTemp, piHumidity, webTemp, webOvercast = row
       print(f"ID: {id}, Date: {date}, Temperature: {piTemp}, Humidity: {piHumidity}, Web Temp: {webTemp}, Cloud Info: {webOvercast}")

    cursor.execute("DELETE FROM data WHERE date < ?",[str(deleteDate)])

    #Commit your changes in the database
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()


value = input("Enter days of db items to keep(ex. 5 means delete any older than 5 days):\n")
validNum = value.isnumeric()
daysToSubtract = int(value)

if (validNum == False):
   print('Invalid number entered')
   quit()

checkYes = input(f'Confirm you want to delete data older than {value} days: Y/N')

if (checkYes.lower() != 'y') and (checkYes.lower() != 'yes'):
    print('Not Deleted')
    quit()

deleteDate = datetime.now() - timedelta(days=daysToSubtract)
deleteDate = deleteDate.replace(microsecond=0)

deleteOldItems()

print('Items Deleted')
