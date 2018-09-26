#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
#import Adafruit GPIO library with alias
import Adafruit_BBIO.GPIO as GPIO ## Solution

#Standard Python Library
import time

def getTimeMS():
    return (int(round(time.time() * 1000)))

# Set pin P9_29 pinmux to gpio
workshop.setPinMux("P9_29","gpio") ## Solution

# Configure P9_29 as a gpio input with an internal pull down
GPIO.setup("P9_29", GPIO.IN,pull_up_down=GPIO.PUD_DOWN) ## Solution



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

    # Read pin P9_29 and set variable "val" to the pins value
    val = GPIO.input("P9_29") ## Solution

    # State 0 wait until button is pressed
    # Add code so if debounce_state is 0 and button is pressed(val=1)
    # print a message, set debounce_state to 1 and save the current 
    # time to the "last_read_gpio" variable
    if debounce_state == 0 and val == 1:
        print "Button pressed" 
        debounce_state = 1
        last_read_gpio = current_time

    # State 1 wait until button has been released
    # Add code so if debounce_state is 1 and button is released(val=0) set debounce_state to 2
    if debounce_state == 1 and val == 0: ## Solution
        debounce_state = 2 ## Solution

    # State 2 wait until debounce time has passed
    # Add code so if debounce_state is 2 and time_delta is greater than gpio_debounce then set debounce_state = 0
    if debounce_state == 2 and time_delta > gpio_debounce: ## Solution
        debounce_state = 0 ## Solution