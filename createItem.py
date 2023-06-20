import Adafruit_DHT
import requests
from datetime import datetime
import time
import greenhouseData
import sqlite3

def writeData():
    # Connect to the SQLite database file
    conn = sqlite3.connect('/home/neal/oopTemp/oopTemp.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Insert the data into the 'data' table
    cursor.execute("INSERT INTO data (date, piTemp, piHumidity, webTemp, webOvercast) VALUES (?, ?, ?, ?, ?)",
                (dataReading.timeOfReading,dataReading.tempReading,dataReading.humidityReading,dataReading.tempFromWeb,dataReading.overCastData))

    # Commit the transaction to save the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

def readWeatherAPI():
    api_url="https://api.openweathermap.org/data/2.5/weather?lat=xxxxx&lon=-xxxxxx&appid=xxxxxxxxxxxxxxxxxxxxxxxxxxx&units=imperial"
    response = None
    i = 0
    while response is None:
      try:
         response = requests.get(api_url)
      except:         
         print("API Request failed, pausing 60 minutes before retry")         
         if i is 6:
            sendError()
            exit
         i += 1
         time.sleep(3600)
    response = requests.get(api_url)
    fullText = response.json()
    localTemp = fullText["main"]["temp"]
    localWeatherList = fullText["weather"]
    localDesc = localWeatherList[0]["description"]

    return localTemp, localDesc

def readSensor():
   DHT_SENSOR = Adafruit_DHT.DHT22
   DHT_PIN = 4   

   humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
   temperature = (temperature * 1.8) + 32

   if humidity is not None and temperature is not None:    
       localTemperature, localDesc = readWeatherAPI()
       # Get the current date and time
       current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       dataReading.setData(current_date,temperature,humidity,localTemperature,localDesc)
       dataReading.displayData()
   else:
       print("Failed to retrieve data from humidity sensor")

#create the object
dataReading = greenhouseData.greenhouseData()

while True:
    readSensor()
    time.sleep(20)
