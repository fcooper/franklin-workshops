#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
#import Adafruit GPIO library with alias
import Adafruit_BBIO.GPIO as GPIO ## Solution

#Standard Python Library
import time

# Use workshop.setPinMux to set "P9_29" to "gpio" mode.
workshop.setPinMux("P9_29","gpio") ## Solution

# Call GPIO.setup and configure "P9_29" as an input with a pull down resistor
GPIO.setup("P9_29", GPIO.IN,pull_up_down=GPIO.PUD_DOWN) ## Solution


while True:
    # Print "Button Pressed" when the button has been pressed
    if GPIO.input("P9_29"): ## Solution
        print "Button Pressed" ## Solution