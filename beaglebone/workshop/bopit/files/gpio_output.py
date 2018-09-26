#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
#import Adafruit GPIO library with alias GPIO
import Adafruit_BBIO.GPIO as GPIO

#Standard Python Library
import time


# Use workshop.setPinMux to set "P9_46" to "gpio" mode.
## PUT YOUR CODE HERE ##

# Call GPIO.setup and configure P9_46 as an output
## PUT YOUR CODE HERE ##


while True:
    # Call GPIO output function and have "P9_46" output high
    ## PUT YOUR CODE HERE ##

    time.sleep(2)

    # Call GPIO output function and have "P9_46" output low
    ## PUT YOUR CODE HERE ##

    time.sleep(2)