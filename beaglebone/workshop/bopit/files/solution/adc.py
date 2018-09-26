#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
#import Adafruit ADC library with alias
import Adafruit_BBIO.ADC as ADC 

#Standard Python Library
import time


# Call ADC Setup (Must be done only once)
ADC.setup() ## Solution

while True:
    # Read ADC pin (P9_36) and set it to variable val
    val = ADC.read("P9_36") ## Solution
 
    # Output ADC value
    print "ADC: ",val ## Solution

    # Convert ADC digital value to analog (voltage) value. Max analog value is 1.8V
    val = val * 1.8 ## Solution

    # Output analog (voltage) value
    print "Voltage: ",val ## Solution

    time.sleep(1)