# ///////////////////////////////////////
# Raspberry Pi 1:                       #
# -BNO055 (orientation) [x1]            #
#  -MMA8451 (accelerometer) [x3]        #
#  -TCA9548A (multiplexer) [x1]         #
# ///////////////////////////////////////

# ///////////////////////////////////////////////////////////////
# code to install libraries for each sensor                     #
# on the pi, write in terminal                                  #
#                                                               #
# BNO055                                                        #
# sudo pip3 install adafruit-circuitpython-bno055               #
#                                                               #
# MMA8451                                                       #
# sudo pip3 install adafruit-circuitpython-mma8451              #
#                                                               #     
# TCA9548A                                                      #
# sudo pip3 install adafruit-circuitpython-tca9548a             #
# https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A   #
# ///////////////////////////////////////////////////////////////

# libraries
import time
import board
import busio
import adafruit_bno055
import adafruit_mma8451
import adafruit_tca9548a   # multiplexer

# initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)

# initialize I2C bus and sensors
sensor = adafruit_bno055.BNO055(i2c)

# create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# create each sensor using the TCA9548A channel instead of the I2C object
tsl1 = adafruit_mma8451.MMA8451(tca[0])   # MMA8451_1
tsl2 = adafruit_mma8451.MMA8451(tca[1])   # MMA8451_2
tsl3 = adafruit_mma8451.MMA8451(tca[2])   # MMA8451_3

# open files for each sensor
bno055_1 = open('/media/pi/bno055_1.txt', 'w')
mma8451_1 = open('/media/pi/mma8451_1.txt', 'w')
mma8451_2 = open('/media/pi/mma8451_2.txt', 'w')
mma8451_3 = open('/media/pi/mma8451_3.txt', 'w')
 
while True:
# BNO055 code
    bno055_1.write('%f\n', sensor.acceleration)
 
 # will talk to Paul G about which other ones to add
     
'''
    print('Temperature: {} degrees C'.format(sensor.temperature))
    print('Accelerometer (m/s^2): {}'.format(sensor.acceleration))
    print('Magnetometer (microteslas): {}'.format(sensor.magnetic))
    print('Gyroscope (rad/sec): {}'.format(sensor.gyro))
    print('Euler angle: {}'.format(sensor.euler))
    print('Quaternion: {}'.format(sensor.quaternion))
    print('Linear acceleration (m/s^2): {}'.format(sensor.linear_acceleration))
    print('Gravity (m/s^2): {}'.format(sensor.gravity))
'''
     
# MMA8451 code
    x1, y1, z1 = tsl1.acceleration
    x2, y2, z2 = tsl2.acceleration
    x3, y3, z3 = tsl3.acceleration
     
    # print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
    mma8451_1.write('%f %f %f\n', x1, y1, z1)
    mma8451_2.write('%f %f %f\n', x2, y2, z2)
    mma8451_3.write('%f %f %f\n', x3, y3, z3)
     
'''
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
'''

# close files
bno055_1.close()
mma8451_1.close()
mma8451_2.close()
mma8451_3.close()
     
# /////////////////////////////////////////////////////////////////
'''
# optional code for MMA8451

# Optionally change the address if it's not the default:
sensor = adafruit_mma8451.MMA8451(i2c, address=0x1C)
 
# Optionally change the range from its default of +/-4G:
sensor.range = adafruit_mma8451.RANGE_2G  # +/- 2G
sensor.range = adafruit_mma8451.RANGE_4G  # +/- 4G (default)
sensor.range = adafruit_mma8451.RANGE_8G  # +/- 8G
 
# Optionally change the data rate from its default of 800hz:
sensor.data_rate = adafruit_mma8451.DATARATE_800HZ  #  800Hz (default)
sensor.data_rate = adafruit_mma8451.DATARATE_400HZ  #  400Hz
sensor.data_rate = adafruit_mma8451.DATARATE_200HZ  #  200Hz
sensor.data_rate = adafruit_mma8451.DATARATE_100HZ  #  100Hz
sensor.data_rate = adafruit_mma8451.DATARATE_50HZ   #   50Hz
sensor.data_rate = adafruit_mma8451.DATARATE_12_5HZ # 12.5Hz
sensor.data_rate = adafruit_mma8451.DATARATE_6_25HZ # 6.25Hz
sensor.data_rate = adafruit_mma8451.DATARATE_1_56HZ # 1.56Hz
'''
