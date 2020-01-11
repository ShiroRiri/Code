# //////////////////////////////////////////
# Raspberry Pi 3                           #
# -BMP388 -> altitude, pressure, temp [x1] #
# -BME280 -> temp, pressure, humidity [x1] #
# -SGP30  -> CO2 [x1]                      #
# -TCA9548A -> Multiplexer [x1]            #
# -Raspberry Pi Camera                     #
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
#                                                             #
# TCA9548A:                                                   #
# sudo pip3 install adafruit-circuitpython-tca9548a           #
#                                                             #
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

camera = PiCamera()


# initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)

# create the TCA object and address it an i2c bus
tca = adafruit_tca9548a.TCA9548A(i2c)

ts11 = adafruit_bmp3xx.BMP3XX(tca[0])
ts12 = adafruit_bme280.BME280(tca[1])
ts13 = adafruit_sgp30.SGP30(tca[2])

# code for BMP388

bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2

while True:
    print("Pressure: {:6.1f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature))
    time.sleep(1)

# code for BME288

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    time.sleep(2)

# code for SGP30
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

elapsed_sec = 0

while True:
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
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
