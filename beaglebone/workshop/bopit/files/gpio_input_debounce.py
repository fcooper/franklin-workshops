#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
import Adafruit_BBIO.GPIO as GPIO

#Standard Python Library
import time

# Configure GPIO
# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!


while True:
    # Print "Button Pressed" when the button has been pressed
    # !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!


# State machine used to implement gpio debounce
# State 0 (button not pressed)
# State 1 (button released)
# State 2 (Debounce for X ms)
debounce_state = 0
# How many ms to wait before reading gpio again
gpio_debounce = 100

# Time last read the gpio
last_read_gpio = None

while True:

    current_time = getTimeMS()
    time_delta = current_time - last_read_gpio

    # Read GPIO
    # !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!

    # Add code so if state is 0 and button is pressed(1) print a message and set state to 1
    # !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!


    # Add code so if state is 1 and button is released(0) set state to 2
    # !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!! 


    # Add code so if state is 2 and debounced time passed set state to 0
    # !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!! 


    time.sleep(1)