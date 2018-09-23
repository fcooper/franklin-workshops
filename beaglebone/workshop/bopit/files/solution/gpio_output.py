#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
#import Adafruit GPIO library with alias
import Adafruit_BBIO.GPIO as GPIO

#Standard Python Library
import time


# Use workshop.setPinMux to set "P9_46" to "gpio" mode.
workshop.setPinMux("P9_46","gpio") ## Solution

# Call GPIO.setup and configure P9_46 as an output
GPIO.setup("P9_46", GPIO.OUT) ## Solution


while True:
    # Call GPIO output function and have "P9_46" output high
    GPIO.output("P9_46", GPIO.HIGH) ## Solution

    time.sleep(2)

    # Call GPIO output function and have "P9_46" output low
    GPIO.output("P9_46", GPIO.LOW) ## Solution

    time.sleep(2)