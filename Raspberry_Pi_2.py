# /////////////////////////////////////////////// #
# Raspberry Pi 2:                                 #
#  - DS18B20 (temp probe) [x4]                    #
#  - strain gauge [x2]                            #
#  - ADS1115 (analog to digital converter) [x2]   #
# /////////////////////////////////////////////// #

# libraries
import time
import board
import busio
import RPi.GPIO as GPIO
import adafruit_ads1x15.ads1115 as ADS
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

from adafruit_onewire.bus import OneWireBus         #import the OneWire Bus
from adafruit_ds18x20 import DS18X20                         #import sensor
from adafruit_ads1x15.analog_in import AnalogIn

# initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize one-wire bus on board pin D5.
ow_bus = OneWireBus(board.D5)

ads = ADS.ADS1115(i2c)

# Scan for sensors and grab the first one found.
ds18_1 = adafruit_ds18x20.DS18X20(ow_bus, devices[0]) #DS18X20_1
ds18_2 = adafruit_ds18x20.DS18X20(ow_bus, devices[1]) #DS18X20_2
ds18_3 = adafruit_ds18x20.DS18X20(ow_bus, devices[2]) #DS18X20_3
ds18_4 = adafruit_ds18x20.DS18X20(ow_bus, devices[3]) #DS18X20_4

# open files for the sensors out here
ds18x20_1_File = open('/mnt/usb/ds18x20_1.txt', 'w')
ds18x20_2_File = open('/mnt/usb/ds18x20_2.txt', 'w')
ds18x20_3_File = open('/mnt/usb/ds18x20_3.txt', 'w')
ds18x20_4_File = open('/mnt/usb/ds18x20_4.txt', 'w')

def data():
# Main loop to print the temperature every second.

   x1 = ds18_1.temperature
   x2 = ds18_2.temperature
   x3 = ds18_3.temperature
   x4 = ds18_4.temperature

   # at some point create an object to write to
   ds18x20_1.write("{}\n".format(x1))
   ds18x20_2.write("{}\n".format(x2))
   ds18x20_3.write("{}\n".format(x3))
   ds18x20_4.write("{}\n".format(x4))
   print(datetime.datetime.utcnow()+datetime.timedelta(hours=-8))
   print()
   time.sleep(1.0)

while True:
  data()

# The callback for when the client receives a CONNACK response from the server.
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
    # more callbacks, etc

# close files
ds18x20_1.close()
ds18x20_2.close()
ds18x20_3.close()
ds18x20_4.close()
