import sqlite3

def readAllDB():
    # Connect to the SQLite database file
    conn = sqlite3.connect('Temp.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Insert the data into the 'data' table    
    cursor.execute("SELECT * FROM data")

    rows = cursor.fetchall()

    # Iterate over the rows and print the data
    for row in rows:
       id, date, piTemp, piHumidity, webTemp, webOvercast = row
       print(f"ID: {id}, Date: {date}, Temperature: {piTemp}, Humidity: {piHumidity}, Web Temp: {webTemp}, Cloud Info: {webOvercast}")

    # Close the cursor and connection
    cursor.close()
    conn.close()

readAllDB()
