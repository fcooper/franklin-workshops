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
state = 0
# How many ms to wait before reading gpio again
gpio_debounce = 100

# Time last read the gpio
last_read_gpio = 0

while True:
    # Important Information
    #   btnVal is used to store pin P9_29 val
    #       btnVal == 1 means button is pressed 
    #       btnVal == 0 means button is pressed 
    #   state is used to determine what the current state is
    #   current_time will store the current time in milliseconds
    #   time_delta will store how much time has past since button was pressed

    current_time = getTimeMS()
    time_delta = current_time - last_read_gpio

    # Read pin P9_29 and set variable "btnVal" to the pins value
    ## PUT YOUR CODE HERE ##

    # See if "state" variable is equal to 0 . If it is do the following:
    #   See if btnVal variable is equal to 1 . If it is do the following:
    #       Print out a message
    #       Set the "state" variable to 1
    #       Set "last_read_gpio" variable to "current_time"
    ## PUT YOUR CODE HERE ##
        ## PUT YOUR CODE HERE ##
            ## PUT YOUR CODE HERE ##
            ## PUT YOUR CODE HERE ##
            ## PUT YOUR CODE HERE ##

    # See if "state" variable is equal to 1. If it is do the following:
    #   See if "btnVal" variable is equal to 0. If it is do the following:
    #       Set the "state" variable to 2
    ## PUT YOUR CODE HERE ##
        ## PUT YOUR CODE HERE ##
            ## PUT YOUR CODE HERE ##

    # See if "state" variable is equal to 2. If it is do the following:
    #   See if "time_delta" variable is greater than "gpio_debounce" variable. If it is do the following:
    #       Set the "state" variable to 0
    if state == 2:
        ## PUT YOUR CODE HERE ##
            ## PUT YOUR CODE HERE ##
