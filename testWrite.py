import Adafruit_DHT
import requests
import time
import sqlite3
from datetime import datetime

def printData(tempReading, humidityReading):
    print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(tempReading, humidityRead
ing))

def printLocalWeather(localTemperature,localDesc):
    print("Outside Temp:{0:0.1f}*F  Weather=".format(localTemperature)+localDesc
)

def readWeatherAPI():
    response = requests.get(api_url)
    fullText = response.json()
    localTemp = fullText["main"]["temp"]
    localWeatherList = fullText["weather"]
    localDesc = localWeatherList[0]["description"]

    return localTemp, localDesc

def writeToDB(piTemp, piHumidity):
    # Connect to the SQLite database file
    conn = sqlite3.connect('/home/user/test/testDB.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Get the current date and time
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Example data (replace with actual sensor data)
    # temperature = piTemp
    # humidity = piHumidity

    # Insert the data into the 'data' table
    cursor.execute("INSERT INTO data (date, temperature, humidity) VALUES (?, ?,?)",(current_date, piTemp, piHumidity))

    # Commit the transaction to save the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()
 

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
api_url="https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={apiKey}&units=imperial"

print ('Program Starting...')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperature = (temperature * 1.8) + 32

    if humidity is not None and temperature is not None:
        printData(temperature, humidity)
        localTemperature, localDesc = readWeatherAPI()
        printLocalWeather(localTemperature, localDesc)
        writeToDB(temperature, humidity)
        time.sleep(20)
    else:
        print("Failed to retrieve data from humidity sensor")

