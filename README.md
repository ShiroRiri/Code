# PAYLOAD - Norco College Rocketry

This is the code for the payload section by Norco College Rocketry.
There is a pi zero in the nosecone acting as a wireless access point for the three raspberry pi boards below in payload proper. There is also an arduino on the ground connected to a radio transceiver.

## Getting Started
The repository is broken down by the python code (.py files) in the code directory.
There are libraries and tutorials required to set up each pi, located below, along with which sensors are being utilized.

## Raspberry Pi Zero

### The Sensors
* RFM96W -> 433 MHz radio transceiver [x1]
* DS18B20 -> temp probe [x1]
* strain gague [x1]
* ADS1115 -> analog to digital converter [x1]

## Raspberry Pi 1
* BNO055   -> accelerometer 1 [x1]
* MMA8451  -> accelerometer 2 [x3]
* TCA9548A -> Multiplexer [x1]

## Raspberry Pi 2
* DS18B20 -> temp probe [x4]
* strain gague [x2]
* ADS1115 -> analog to digital converter [x2]
* TCA9548A -> Multiplexer [x1]

## Raspberry Pi 3
* BMP388 -> altitude, pressure, temp [x1]
* BME280 -> temp, pressure, humidity [x1]
* SGP30  -> CO2 [x1]
* TCA9548A -> Multiplexer [x1]
* Raspberry Pi Camera

## Arduino
