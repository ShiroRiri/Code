'''
NORCO COLLEGE ROCKETRY
This is the code for the Raspberry Pi Zero in the nosecone.
It is in infrastructure mode as a wireless access point
that the Pi boards below will connect to. When they do
they will send a message.
'''

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
#MQTT_SERVER = "192.168.4.1"
MQTT_PATH_COMMAND = "command_channel"
MQTT_PATH_REPLY = "reply_channel"

# command list
# 1. ONLINE
# 2. START DATA ACQUISITION
# 3. STOP DATA ACQUISITION
# 4. POWER OFF

def on_connect(client, userdata, flags, rc):
        print("Connected to client with result code " +str(rc))
        client.subscribe(MQTT_PATH_REPLY)
        publish.single(MQTT_PATH_COMMAND, "ONLINE", hostname=MQTT_SERVER)
#        client.publish(MQTT_PATH_COMMAND, "ONLINE")

def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
