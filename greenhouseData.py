class greenhouseData(object):
    def __init__(self):
        self.timeOfReading = ""
        self.tempReading = 0
        self.humidityReading = 0
        self.tempFromWeb = 0
        self.overCastData = ""
    
    def setData(self,timeOfReading,tempReading,humidityReading,tempFromWeb,overCastData):
        self.timeOfReading = timeOfReading
        self.tempReading = tempReading
        self.humidityReading = humidityReading
        self.tempFromWeb = tempFromWeb
        self.overCastData = overCastData

    def displayData(self):
        print("Temperature From Sensor: " + self.timeOfReading)
        print("Temperature From Sensor: {0:0.1f}F".format(self.tempReading))
        print("Humidity From Sensor   : {0:0.1f}%".format(self.humidityReading))
        print("Temperature From Web   : {0:0.1f}F".format(self.tempFromWeb))
        print("Cloud Cover Data       : " + self.overCastData)
