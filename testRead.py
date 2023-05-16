import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('/home/user/test/testDB.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve all rows from the 'data' table
cursor.execute("SELECT * FROM data")

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Iterate over the rows and print the data
for row in rows:
    date, temperature, humidity = row
    print(f"Date: {date}, Temperature: {temperature}, Humidity: {humidity}")

# Close the cursor and connection
cursor.close()
conn.close()
