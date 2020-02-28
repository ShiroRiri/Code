# //////////////////////////////////////////
# Raspberry Pi 3                           #
# -BMP388 -> altitude, pressure, temp [x1] #
# -BME280 -> temp, pressure, humidity [x1] #
# -SGP30  -> CO2 [x1]                      #
# //////////////////////////////////////////

# /////////////////////////////////////////////////////////////
# code to install proper libraries for each sensor            #
# on the pi, write in terminal                                #
#                                                             #
# BMP388:                                                     #
# sudo pip3 install adafruit-circuitpython-bmp3xx             #
#                                                             #
# BME280:                                                     #
# sudo pip3 install adafruit-circuitpython-bme280             #
#                                                             #
# SGP30:                                                      #
# sudo pip3 install adafruit-circuitpython-sgp30              #
# /////////////////////////////////////////////////////////////

#libraries
import time
import board
import busio
import adafruit_bmp3xx
import adafruit_bme280
import adafruit_sgp30
import adafruit_tca9548a
from picamera import PiCamera
from time import sleep

# ////////////////////////////////////////////////////////////////////////////////

# initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)

#Create library on I2C port
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

#open files for each sensor
bmp3xx = open('/home/pi/NCR/Read/bmp3xx.txt', 'w') #txt file needs to be created on Pi
bme280 = open('/home/pi/NCR/Read/bme280.txt', 'w') #txt file needs to be created on Pi
sgp30 = open('/home/pi/NCR/Read/sgp30.txt', 'w') #txt file needs to be created on Pi
    
bmp_temp = bmp3xx.temperature
bmp_press = bmp3xx.pressure
bme_temp = bme280.temperature
bme_hum = bme280.humidity
bme_press = bme280.pressure
bme_alt = bme280.altitude
sgp_CO2 = sgp30.eCO2
sgp_TVOC = sgp30.TVOC

bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2

while True:
    print("Pressure: {:6.1f}  Temperature: {:5.2f}".format(bmp_press, bmp_temp))
    time.sleep(1)

# code for BME288

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme_temp)
    print("Humidity: %0.1f %%" % bme_hum)
    print("Pressure: %0.1f hPa" % bme_press)
    print("Altitude = %0.2f meters" % bme_alt)
    time.sleep(2)

# code for SGP30
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

elapsed_sec = 0

while True:
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp_CO2, sgp_TVOC))
    time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))

# code for camera
camera.start_preview()
sleep()
camera.capture() #add a pathway here later
sleep(5)

#close files
bmpx33.close()
bme280.close()
sgp30.close()
