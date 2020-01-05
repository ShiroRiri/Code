# ///////////////////////////////////////
# Raspberry Pi 1:                       #
# -BNO055   -> accelerometer 1 [x1]     #
# -MMA8451  -> accelerometer 2 [x3]     #
# -TCA9548A -> Multiplexer [x1]         #
# ///////////////////////////////////////

# BNO055
# sudo pip3 install adafruit-circuitpython-bno055

# code for BNO055
import time
import board
import busio
import adafruit_bno055
 
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)
 
while True:
    print('Temperature: {} degrees C'.format(sensor.temperature))
    print('Accelerometer (m/s^2): {}'.format(sensor.acceleration))
    print('Magnetometer (microteslas): {}'.format(sensor.magnetic))
    print('Gyroscope (rad/sec): {}'.format(sensor.gyro))
    print('Euler angle: {}'.format(sensor.euler))
    print('Quaternion: {}'.format(sensor.quaternion))
    print('Linear acceleration (m/s^2): {}'.format(sensor.linear_acceleration))
    print('Gravity (m/s^2): {}'.format(sensor.gravity))
    print()
 
    time.sleep(1)
