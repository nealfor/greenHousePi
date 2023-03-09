import Adafruit_DHT
import requests
import time

def printData(tempReading, humidityReading):
    print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(tempReading, humidityReading))

def printLocalWeather(localTemperature,localDesc):
    print("Outside Temp:{0:0.1f}*F  Weather=".format(localTemperature)+localDesc)

def readWeatherAPI():
    response = requests.get(api_url)
    fullText = response.json()
    localTemp = fullText["main"]["temp"]
    localWeatherList = fullText["weather"]
    localDesc = localWeatherList[0]["description"]

    return localTemp, localDesc


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
api_url="https://api.openweathermap.org/data/2.5/weather?lat=XXXXXX&lon=XXXXXXXX&appid=XXXXXXXXXXXXX&units=imperial"


while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        printData(temperature, humidity)
        localTemperature, localDesc = readWeatherAPI()
        printLocalWeather(localTemperature, localDesc)
        time.sleep(20)
    else:
        print("Failed to retrieve data from humidity sensor")


