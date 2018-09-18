#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
#import Adafruit GPIO library with alias
## PUT YOUR CODE HERE ##

#Standard Python Library
import time

def getTimeMS():
    return (int(round(time.time() * 1000)))

# Set pin P9_29 pinmux to gpio
## PUT YOUR CODE HERE ##

# Configure P9_29 as a gpio input with an internal pull down
## PUT YOUR CODE HERE ##



# State machine used to implement gpio debounce
# State 0 (button not pressed)
# State 1 (button released)
# State 2 (Debounce for X ms)
debounce_state = 0
# How many ms to wait before reading gpio again
gpio_debounce = 100

# Time last read the gpio
last_read_gpio = 0

while True:

    current_time = getTimeMS()
    time_delta = current_time - last_read_gpio

    # Read pin P9_29
    ## PUT YOUR CODE HERE ##

    # Add code so if debounce_state is 0 and button is pressed(val=1) print a message and set debounce_state to 1
    if debounce_state == 0 and val == 1:
        print "Button pressed" 
        debounce_state = 1
        last_read_gpio = current_time


    # Add code so if debounce_state is 1 and button is released(val=0) set debounce_state to 2
    ## PUT YOUR CODE HERE ##
        ## PUT YOUR CODE HERE ##

    # Add code so if debounce_state is 2 and time_delta is greater than gpio_debounce then set debounce_state = 0
    ## PUT YOUR CODE HERE ##
        ## PUT YOUR CODE HERE ##
