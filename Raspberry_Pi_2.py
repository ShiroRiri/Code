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
# ///////////////////////////////////////////////////////////////

# libraries
import board
import busio

# 
i2c = busio.I2C(board.SCL, board.SDA)
