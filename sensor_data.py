import grovepi
import math
import time

dht_sensor = 4  # temp/humidity sensor -> digital port 4
sound_sensor = 0 # sound sensor -> analog port A0
grovepi.pinMode(sound_sensor, "INPUT") # threshold: __



def handleDht():
    try:
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type of sensor (change to 1 for white sensor).
        [temp,humidity] = grovepi.dht(dht_sensor,0)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))

    except IOError:
        print ("Error in handleDht()")

def handleLoudness(): # look into frequency / how often it is picking up signal 
    try:
        # read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)

        #determine the noise level based on sensor val
        if sensor_value < 250:
            print("very little environmental noise")
        elif 251 <= sensor_value <= 400:
            print("moderate environmental noise")
        elif 401 <= sensor_value <= 580:
            print("high environmental noise")
        else:
            print("very loud environmental noise")

        time.sleep(.5)

    except IOError:
        print("Error in handleLoudness()")

while True:
    handleDht()
    handleLoudness()
    time.sleep(5)
    