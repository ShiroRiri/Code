# //////////////////////////////////////////
# Raspberry Pi 3                           #
# -BMP388 -> altitude, pressure, temp [x1] #
# -BME280 -> temp, pressure, humidity [x1] #
# -SGP30  -> CO2 [x1]                      #
# //////////////////////////////////////////

#libraries
import time
import board
import busio
import adafruit_bmp3xx
import adafruit_bme280
import adafruit_sgp30

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.4.1"
MQTT_PATH_COMMAND = "command_channel"
MQTT_PATH_REPLY = "reply_channel"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# initialize I2C bus and sensors
i2c = busio.I2C(board.SCL, board.SDA)

# create library on I2C port
bmp388 = adafruit_bmp3xx.BMP3XX_I2C(i2c, address = 0x76)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

# set variables for each sensor value
bmp_temp = bmp388.temperature
bmp_press = bmp388.pressure
bme_temp = bme280.temperature
bme_hum = bme280.humidity
bme_press = bme280.pressure
bme_alt = bme280.altitude
sgp_CO2 = sgp30.eCO2
sgp_TVOC = sgp30.TVOC

# base case
bmp388.pressure_oversampling = 8
bmp388.temperature_oversampling = 2
bme280.sea_level_pressure = 1013.25
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

# open files for each sensor
bmp388_file = open('/mnt/usb/bmp388.txt', 'w')
bme280_file = open('/mnt/usb/bme280.txt', 'w')
sgp30_file  = open('/mnt/usb/sgp30.txt', 'w')

def data():
    bmp388_file.write("{},{}\n".format(bmp_temp, bmp_press))
    bme280_file.write("{},{},{},{}\n".format(bme_temp, bme_hum, bme_press, bme_alt))
    sgp30_file.write("{},{}\n".format(sgp_CO2, sgp_TVOC))

    '''
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
    '''

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

#close files
bmp388_file.close()
bme280_file_file.close()
sgp30_file.close()
