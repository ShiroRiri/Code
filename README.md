# PAYLOAD - Norco College Rocketry

This is the code for the payload section by Norco College Rocketry.\
There is a pi zero in the nosecone acting as a wireless access point for the three raspberry pi boards below in payload proper. There is also an arduino on the ground connected to a radio transceiver.

### Getting Started
The repository is broken down by the python code (.py files) in the code directory.\
There are libraries and tutorials required to set up each pi, located below, along with which sensors are being utilized.

## Raspberry Pi Zero
This one is a little more involved.
### MQTT
This is how our server/client communicate.\
```
sudo apt-get install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl status mosquitto
sudo pip install paho-mqtt
```
You can test if it is working locally with there 2 in 2 different terminals:
```
mosquitto_sub -h localhost -t "test/message"
mosquitto_pub -h localhost -t "test/message" -m "Hello, world"
```
Here are the tutorials I used: \
https://tutorials-raspberrypi.com/raspberry-pi-mqtt-broker-client-wireless-communication/ \
https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi \  

\Here is a good reference
https://pypi.org/project/paho-mqtt/


### Wireless access point
Follow this raspberry pi official tutorial to get it working\
https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md

* RFM96W -> 433 MHz radio transceiver [x1]
* DS18B20 -> temp probe [x1]
* strain gague [x1]
* ADS1115 -> analog to digital converter [x1]

## Raspberry Pi 1
### BNO055   -> accelerometer 1 [x1]
```
sudo pip3 install adafruit-circuitpython-bno055
```
### MMA8451  -> accelerometer 2 [x3]
```
sudo pip3 install adafruit-circuitpython-mma8451
```
### TCA9548A -> Multiplexer [x1]
```
sudo pip3 install adafruit-circuitpython-tca9548a
```
Here is the GitHub link for the reference code\
https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A
### Raspberry Pi Camera
```
 
```

## Raspberry Pi 2
### DS18B20 -> temp probe [x4]
```
sudo pip3 install adafruit-circuitpython-onewire
sudo pip3 install adafruit-circuitpython-ds18x20 
```
### ADS1115 -> analog to digital converter [x2]
```
sudo pip3 install adafruit-circuitpython-ads1x15
```
### TCA9548A -> Multiplexer [x1]
```
sudo pip3 install adafruit-circuitpython-tca9548a
```
Here is a useful link for the multiplexer\
https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A
* strain gague [x2]

## Raspberry Pi 3
### BMP388 -> altitude, pressure, temp [x1]
```
sudo pip3 install adafruit-circuitpython-bmp3xx
```
### BME280 -> temp, pressure, humidity [x1]
```
sudo pip3 install adafruit-circuitpython-bme280
```
### SGP30  -> CO2 [x1]
```
sudo pip3 install adafruit-circuitpython-sgp30
```
### TCA9548A -> Multiplexer [x1]
```
sudo pip3 install adafruit-circuitpython-tca9548a
```
Here is a useful link for the multiplexer\
https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A

## Arduino
