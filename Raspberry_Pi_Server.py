import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.4.1"
MQTT_PATH = "command_channel"
MQTT_PATH_REPLY = "reply_channel"

#####

def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(MQTT_PATH_REPLY)
        client.publish(MQTT_PATH, "Hello World!")

def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()

#############################################################################################

'''

'''
NORCO COLLEGE ROCKETRY
This is the code for the Raspberry Pi Zero in the nosecone.
It is in infrastructure mode as a wireless access point
that the Pi boards below will connect to. When they do
they will send a message.
'''

import paho.mqtt.publish as publish
import time

MQTT_SERVER = "localhost"
MQTT_PATH = "test/channel"

command_systems_online = 1
command_initiate_startup_sequence = 2
command_get_altitude = 3
command_stop_sequence = 4
command_power_off = 5

# run through and send each command
publish.single(MQTT_PATH, command_systems_online, hostname=MQTT_SERVER)
time.sleep(3)

'''
publish.single(MQTT_PATH, command_initiate_startup_sequence, hostname=MQTT_SERVER)
time.sleep(3)

publish.single(MQTT_PATH, command_get_altitude, hostname=MQTT_SERVER)
time.sleep(3)

publish.single(MQTT_PATH, command_stop_sequence, hostname=MQTT_SERVER)
time.sleep(3)

publish.single(MQTT_PATH, command_power_off, hostname=MQTT_SERVER)
time.sleep(3)
'''

'''