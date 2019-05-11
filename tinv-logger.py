#!/usr/bin/python
import time
import datetime
from Adafruit_BMP085 import BMP085

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

#temp = bmp.readTemperature()

# Read the current barometric pressure level
#pressure = bmp.readPressure()

# To calculate altitude based on an estimated mean sea level pressure
# (1013.25 hPa) call the function as follows, but this won't be very accurate
#altitude = bmp.readAltitude()

# To specify a more accurate altitude, enter the correct mean sea level
# pressure level.  For example, if the current pressure level is 1023.50 hPa
# enter 102350 since we include two decimal places in the integer value
# altitude = bmp.readAltitude(102350)
text_file = open("logs/"+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+".txt", "a")

while True:
    temp = format(bmp.readTemperature(), '.2f')
    pressure = format(bmp.readPressure() / 100, '.2f')
    altitude = format(bmp.readAltitude(100500), '.2f') #input sea level pressure to calibrate alt
    ts = time.time()
    stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')
    print "Temperature: " + temp + " C"
    print "Pressure:    " + pressure + " hPa"
    print "Altitude:    " + altitude + "% meters"
    print "Timestamp:   " + stamp
    print "---------------------------------"
    log = str(temp) + "," + str(pressure) + "," + str(altitude) + "," + str(stamp)
    text_file.write(log + "\n")
    time.sleep(0.2)
    
text_file.close()
