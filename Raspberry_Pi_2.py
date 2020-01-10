# /////////////////////////////////////////////// #
# Raspberry Pi 2:                                 #
#  - DS18B20 (temp probe) [x4]                    #
#  - strain gague [x2]                            #
#  - ADS1115 (analog to digital converter) [x2]   #
# /////////////////////////////////////////////// #

# ///////////////////////////////////////////////////////////////
# code to install libraries for each sensor                     #
# on the pi, write in terminal                                  #
#                                                               #
# ADS1115                                                       #
# sudo pip3 install adafruit-circuitpython-ads1x15              #
#                                                               #
# DS18B20                                                       #
# sudo pip3 install adafruit-circuitpython-onewire              #
# sudo pip3 install adafruit-circuitpython-ds18x20              #
#                                                               #
# ADS1115                                                       #
# sudo pip3 install adafruit-circuitpython-ads1x15              #
# ///////////////////////////////////////////////////////////////

# libraries
import time
import board
import busio

# set up temperature probe for analog
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

# initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize one-wire bus on board pin D5.
ow_bus = OneWireBus(board.D5)                                   # fix this

# Scan for sensors and grab the first one found.
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
 
# Main loop to print the temperature every second.
while True:
    print('Temperature: {0:0.3f}C'.format(ds18.temperature))
    time.sleep(1.0)
