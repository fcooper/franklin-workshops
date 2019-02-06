#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
#import Adafruit ADC library with alias
import Adafruit_BBIO.ADC as ADC 

#Standard Python Library
import time


# Call ADC Setup (Must be done only once)
## PUT YOUR CODE HERE ##

while True:
    # Read ADC value from pin (P9_36) and set retrieved value to variable called "val"
    ## PUT YOUR CODE HERE ##
 
    # Print value of "val" variable
    ## PUT YOUR CODE HERE ##

    # Convert digital value stored in "val" variable to analog (voltage) value.
    # Store the converted value back into "val" variable.
    # Important note: Max analog value possible is 1.8V
    ## PUT YOUR CODE HERE ##

    # Print value of "val" variable (should contain analog value from (0 - 1.8V)
    ## PUT YOUR CODE HERE ##

    time.sleep(1)