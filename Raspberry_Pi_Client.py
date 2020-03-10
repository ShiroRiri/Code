'''
NORCO COLLEGE ROCKETRY
This is the code for Raspberry Pi 1 in the payload of the rocket.
'''

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.4.1"
MQTT_PATH_COMMAND = "command_channel"
MQTT_PATH_REPLY = "reply_channel"

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

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()



















##################################################################################

'''
'''
NORCO COLLEGE ROCKETRY
This is the code for Raspberry Pi 1 in the payload of the rocket.
'''

import paho.mqtt.client as mqtt
import time

# the server is the static IP of the pi zero in the nosecone
MQTT_SERVER = "192.168.4.1"
MQTT_PATH = "test/channel"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
        print("Raspberry Pi 1 is connected\nwith result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
        print(str(msg.payload)+" on channel: "+msg.topic)
#       switch(msg.payload)

        print("\n")
#       print(msg.topic+" "+str(msg.payload))

'''
def message_1():
        print("Raspberry Pi 1 is online")
def message_2():
        print("Initiating startup sequence")
def message_3():
        print("Altitude: ")
def message_4():
        print("Raspberry Pi 1 entering idle state")
def message_5():
        print("Powering off Raspberry Pi 1")

def switch(message):
        swtch = {
                1 : message_1(),
                2 : message_2(),
                3 : message_3(),
                4 : message_4(),
                5 : message_5()
        }.get(message, 'default')
'''

client = mqtt.Client()
client.on_connect = on_connect

client.on_message = on_message

# these are default parameters
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

'''
