# ///////////////////////////////////////
# Raspberry Pi 1:                       #
# -BNO055   -> accelerometer 1 [x1]     #
# -MMA8451  -> accelerometer 2 [x3]     #
# -TCA9548A -> Multiplexer [x1]         #
# ///////////////////////////////////////

# /////////////////////////////////////////////////////
# code to install libraries for each sensor           #
# on the pi, write in terminal                        #
#                                                     #
# BNO055                                              #
# sudo pip3 install adafruit-circuitpython-bno055     #
#                                                     #
# MMA8451                                             #
# sudo pip3 install adafruit-circuitpython-mma8451    #
# /////////////////////////////////////////////////////

# libraries
import time
import board
import busio
import adafruit_bno055
import adafruit_mma8451
import adafruit_tca9548a   # multiplexer

# ///////////////////////////////////////////////////

# I will finish this tomorrow, night
# https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A

# initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)

# create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# code for BNO055

# initialize I2C bus and sensors
# sensor1 = adafruit_bno055.BNO055(i2c)
# sensor2 = adafruit_mma8451.MMA8451(i2c)

# create each sensor using the TCA9548A channel instead of the I2C object
tsl1 = adafruit_tsl2591.TSL2591(tca[0])   # BNO055
tsl2 = adafruit_tsl2591.TSL2591(tca[1])   # MMA8451 
 
while True:
# BNO055 code
    print('Temperature: {} degrees C'.format(tsl1.temperature))
    print('Accelerometer (m/s^2): {}'.format(tsl1.acceleration))
    print('Magnetometer (microteslas): {}'.format(tsl1.magnetic))
    print('Gyroscope (rad/sec): {}'.format(tsl1.gyro))
    print('Euler angle: {}'.format(tsl1.euler))
    print('Quaternion: {}'.format(tsl1.quaternion))
    print('Linear acceleration (m/s^2): {}'.format(tsl1.linear_acceleration))
    print('Gravity (m/s^2): {}'.format(tsl1.gravity))
    print()
    
# MMA8451 code
    x, y, z = tsl2.acceleration
    print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
    orientation = tsl2.orientation
    # Orientation is one of these values:
    #  - PL_PUF: Portrait, up, front
    #  - PL_PUB: Portrait, up, back
    #  - PL_PDF: Portrait, down, front
    #  - PL_PDB: Portrait, down, back
    #  - PL_LRF: Landscape, right, front
    #  - PL_LRB: Landscape, right, back
    #  - PL_LLF: Landscape, left, front
    #  - PL_LLB: Landscape, left, back
    print('Orientation: ', end='')
    if orientation == adafruit_mma8451.PL_PUF:
        print('Portrait, up, front')
    elif orientation == adafruit_mma8451.PL_PUB:
        print('Portrait, up, back')
    elif orientation == adafruit_mma8451.PL_PDF:
        print('Portrait, down, front')
    elif orientation == adafruit_mma8451.PL_PDB:
        print('Portrait, down, back')
    elif orientation == adafruit_mma8451.PL_LRF:
        print('Landscape, right, front')
    elif orientation == adafruit_mma8451.PL_LRB:
        print('Landscape, right, back')
    elif orientation == adafruit_mma8451.PL_LLF:
        print('Landscape, left, front')
    elif orientation == adafruit_mma8451.PL_LLB:
        print('Landscape, left, back')
 
    time.sleep(1)

  
# /////////////////////////////////////////////////////////////////
# optional code for MMA8451
#
# Optionally change the address if it's not the default:
#sensor = adafruit_mma8451.MMA8451(i2c, address=0x1C)
 
# Optionally change the range from its default of +/-4G:
#sensor.range = adafruit_mma8451.RANGE_2G  # +/- 2G
#sensor.range = adafruit_mma8451.RANGE_4G  # +/- 4G (default)
#sensor.range = adafruit_mma8451.RANGE_8G  # +/- 8G
 
# Optionally change the data rate from its default of 800hz:
#sensor.data_rate = adafruit_mma8451.DATARATE_800HZ  #  800Hz (default)
#sensor.data_rate = adafruit_mma8451.DATARATE_400HZ  #  400Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_200HZ  #  200Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_100HZ  #  100Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_50HZ   #   50Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_12_5HZ # 12.5Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_6_25HZ # 6.25Hz
#sensor.data_rate = adafruit_mma8451.DATARATE_1_56HZ # 1.56Hz
