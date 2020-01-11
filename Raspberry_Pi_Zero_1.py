# /////////////////////////////////////////////// #
# Pi Zero 1                                       #
#  - RFM96W - 433 MHz radio transceiver           #
#  - DS18B20 -temp probe [x1]                     #
#  - DS18B20 -stain gauge[x1]                     #
#  - ADS1115 - analog to digital converter [x1]   #
# /////////////////////////////////////////////// #

# ///////////////////////////////////////////////////////////////
# code to install libraries for each sensor                     #
#                                                               #
# RFM699(w)  -look into this                                    #      
# sudo pip3 install adafruit-circuitpython-rfm69                #
#                                                               #
# ADS1115                                                       #
# sudo pip3 install adafruit-circuitpython-ads1x15              #
# ///////////////////////////////////////////////////////////////


import board
import busio
import digitalio
import adafruit_ads1x15.ads1115 as ADS  #for temp probe ads1115
# for the analog conversion
import board 
import analogio 
adc = analogio.AnalogIn(board.A0) 


# it states spi but we can chagnge it to i2c
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# i2c = busio.I2C(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# defining the boards (CS and RST pins)
cs = digitalio.DigitalInOut(board.D5)
reset = digitalio.DigitalInOut(board.D6)

# specifying the specified--confirmed
import adafruit_rfm69
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, 433.0) #potential swap to I2C

# example message
rfm69.send('Test Code!')

# recieveing message 
rfm69.receive()

# pause time, wait 1 second
rfm69.receive(timeout_s=1.0)  

# If we would like to convert a byte string into an ASCII text string
#-------------------------------------------------------------------------------
packet = rfm69.receive()  # Wait for a packet to be received (up to 0.5 seconds)
if packet is not None:
    packet_text = str(packet, 'ascii')
    print('Received: {0}'.format(packet_text))
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# code for the ads1115
# final import for the ADS1x15 library's version of AnalogIn
from adafruit_ads1x15.analog_in import AnalogIn

# create the ADC object
ads = ADS.ADS1115(i2c)

# we can use two types of mode Single Ended or Differential 

# code for Single Ended mode
chan = AnalogIn(ads, ADS.P0) 

# if we want to set up adddition channels, we keep the same syntax
# but all we have to do is change the pin

# print the amount of voltage
print(chan.value, chan.voltage)

# Differential Mode
# we will need 20 pings for this to work
chan = AnalogIn(ads, ADS.P0, ADS.P1)

# getting the readings
print(chan.value, chan.voltage)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# test value for ADC (analog to digital conversion)
#set test value (either or)
>>> adc.value
32683

>>> adc.value
65

# reference voltage used by the ADC to convert voltages into numbers 
>>> adc.value / 65535 * adc.reference_voltage
3.2998

# we can also make a python function to call the ADC easier
>>> def adc_to_voltage(val):
...   return val / 65535 * 3.3
>>> adc_to_voltage(adc.value)
3.2998
