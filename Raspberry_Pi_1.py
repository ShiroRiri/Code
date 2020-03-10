# ///////////////////////////////////////
# Raspberry Pi 1:                       #
#  -BNO055 (orientation) [x1]           #
#  -MMA8451 (accelerometer) [x3]        #
#  -TCA9548A (multiplexer) [x1]         #
# ///////////////////////////////////////

# libraries
import time
import board
import busio
import adafruit_mma8451
import adafruit_tca9548a
import adafruit_bno055
import threading
import datetime

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.4.1"
MQTT_PATH_COMMAND = "command_channel"
MQTT_PATH_REPLY = "reply_channel"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# initialize I2C bus and sensors for mma8451
i2c = busio.I2C(board.SCL, board.SDA)

# create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# create each sensor using the TCA9548A channel instead of the I2C object
mma8451_1 = adafruit_mma8451.MMA8451(tca[0])   # MMA8451_1
mma8451_2 = adafruit_mma8451.MMA8451(tca[1])   # MMA8451_2
mma8451_3 = adafruit_mma8451.MMA8451(tca[2])   # MMA8451_3
bno055 = adafruit_bno055.BNO055(i2c)

# open files for each sensor
mma8451_1_File = open('/mnt/usb/mma8451_1.txt', 'w')
mma8451_2_File = open('/mnt/usb/mma8451_2.txt', 'w')
mma8451_3_File = open('/mnt/usb/mma8451_3.txt', 'w')
bno055_File = open('/mnt/usb/bno055.txt', 'w')

def data():
    x1, y1, z1 = mma8451_1.acceleration
    x2, y2, z2 = mma8451_2.acceleration
    x3, y3, z3 = mma8451_3.acceleration
    orientation_1 = mma8451_1.orientation
    orientation_2 = mma8451_2.orientation
    orientation_3 = MMA8451_3.orientation
    temp = bno055.temperature
    accel = bno055.acceleration
    mag = bno055.magnetic
    gyr = bno055.gyro
    eul = bno055.euler
    quat = bno055.quaternion
    lin_accel = bno055.linear_acceleration
    grav = bno055.gravity

    mma8451_1_File.write("{},{},{},{}\n".format(x1, y1, z1, orientation_1))
    mma8451_2_File.write("{},{},{},{}\n".format(x2, y2, z2, orientation_2))
    mma8451_3_File.write("{},{},{},{}\n".format(x3, y3, z3, orientation_3))
    bno055_File.write("{},{},{},{},{},{},{},{}\n".format(temp, accel, mag, gyr, eul, quat, lin_accel, grav))

#    print(datetime.datetime.utcnow()+datetime.timedelta(hours=-8))

while True:
    data()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH_COMMAND)
    #client.subscribe(MQTT_PATH_REPLY)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    client.publish(MQTT_PATH_REPLY, "Raspberry Pi 1 is ONLINE")

# close files
mma8451_1.close()
mma8451_2.close()
mma8451_3.close()

#remember to take out the reset pin or else this thing wont work...
#when put in PCB's set reset to high on multiplexer
