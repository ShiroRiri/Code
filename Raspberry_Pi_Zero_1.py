import sys
import threading
import board
import busio
import digitalio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ds18x20 import DS18X20
from adafruit_onewire.bus import OneWireBus
from bintools import DataLogWriter, FieldTypes

# If script is directly called, start main
if __name__ == "__main__":
    main()

def main():
    i2cWriter = DataLogWriter('~/i2c-log.bin', [{'name': 'StrainGuage', 'type': FieldTypes.FLOAT}])
    owWriter = DataLogWriter('~/ow-log.bin', [{'name': 'TempProbe', 'type': FieldTypes.FLOAT}])

    initializeIO()
    startLogging()

def initializeIO():
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ow_bus = OneWireBus(board.D4)
        
        # Initialize devices
        global adc
        global temp_sensor
        global temp_sensor_enable
        adc = ADS.ADS1115(i2c)
        temp_sensor = DS18X20(ow_bus, ow_bus.scan()[0])
        temp_sensor.resolution = 9 # Speeds up the polling rate while sacrificing some resolution
        
        # Strain guage enable transistor
        sg_enable = digitalio.DigitalInOut(D17)
        sg_enable.direction = digitalio.Direction.OUTPUT
        sg_enable.value = False

        print("IO successfully initialized")

    except Exception as e:
        print("Error while initializing IO - {}\n".format(e.message))
        sys.exit(1)

# Threading utilized to ensure maximum throughput on all IO buses
def startLogging(): 
    print("Starting logging threads...")

    # Create logging threads
    i2cThread = threading.Thread(target = logI2CDevices, name = 'i2c-logger')
    owThread = threading.Thread(target = logOWDevices, name = 'ow-logger')

    # Start both threads
    i2cThread.start()
    owThread.start()

    # Ensure script doesn't exit until both are finished
    i2cThread.join()
    owThread.join()

def logI2CDevices():
    sg_enable.value = True # Enable strain guage before ADC samples
    
    while True:
        i2cWriter.beginSample()
        adc_sample = AnalogIn(adc, 0, 1)
        i2cWriter.log(adc_sample.voltage)
        i2cWriter.endSample()

def logOWDevices():
    while True:
        owWriter.beginSample()
        owWriter.log(temp_sensor.temperature())
        owWriter.endSample()
