#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
# import required gpio library with alias
# GPIO Code below
import Adafruit_BBIO.GPIO as GPIO
# import required adc library with alias
# ADC Code below
import Adafruit_BBIO.ADC as ADC
from flask import Flask
from flask_cors import CORS
# import required i2c/smbus library
# I2C Code below
import smbus

#Standard Python Library
import math
import random
import thread
import time


bus = None

def convertToU16(value,little_endian=True):
    value = value & 0xFFFF
    
    if not little_endian:
        value = ((value << 8) & 0xFF00) + (value >> 8)
    return value
    
def getTimeMS():
    return (int(round(time.time() * 1000)))


def gpioSetup(): 
    # dummy place holder
    x = 0

    # Configure pinmux for GPIO connected to push button
    workshop.setPinMux("P9_29","gpio") ## Solution
    # Configure gpio connected to push button as an input with a pull down
    GPIO.setup("P9_29", GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  ## Solution


def getPushButtonVal():
    val = -1

    # Read value of push button gpio and sets its value to "val" variable
    val =  GPIO.input("P9_29")  ## Solution

    return val

def adcSetup():
    # dummy place holder
    x = 0

    # Call ADC Setup
    ADC.setup() ## Solution 

def readPotentiometerVal():
    val = 3000

    # Read the raw adc value from pin connected to potentiometer
    val = ADC.read_raw("P9_36") ## Solution

    return val


# I2C address options
TSL2561_I2C_ADDR          = (0x29)    # Default address (pin left floating)

TSL2561_COMMAND_BIT         = (0x80)    # Must be 1
TSL2561_WORD_BIT            = (0x20)    # 1 = read/write word (rather than byte)

TSL2561_CONTROL_POWERON     = (0x03)
TSL2561_CONTROL_POWEROFF    = (0x00)

TSL2561_REGISTER_CONTROL    = 0x00

TSL2561_DELAY_INTTIME_13MS  = (15) / 1000
TSL2561_REGISTER_CHAN0_LOW  = 0x0C

def i2cSetup():
    global bus
    # I2C

    #Configure i2c pinmux for both of the required i2c pins
    workshop.setPinMux("P9_19","i2c")  ## Solution
    workshop.setPinMux("P9_20","i2c")  ## Solution

    #Initialize I2C Bus 2 and save the object returned to the variable "bus"
    bus = smbus.SMBus(2)  ## Solution

    # Via I2C tell TSL2561 to power off
    bus.write_byte_data(TSL2561_I2C_ADDR,TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL, TSL2561_CONTROL_POWEROFF)  ## Solution

    #Wait 1 Sec
    time.sleep(1)

    # Via I2C command tell TSL2561 to power off
    bus.write_byte_data(TSL2561_I2C_ADDR, TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL, TSL2561_CONTROL_POWERON)  ## Solution

    #Wait 1 Sec
    time.sleep(1)

def getLightValue():
    val = -1

    # Read light intensity value from TSL2561
    val = bus.read_word_data(TSL2561_I2C_ADDR,TSL2561_COMMAND_BIT | TSL2561_WORD_BIT | TSL2561_REGISTER_CHAN0_LOW)   ## Solution

    # convert the value returned to an unsigned 16 bit value
    val = convertToU16(val)   ## Solution

    # return the value read from sensor
    return val


checked = True
response = "Nothing"

# State machine used to implement gpio debounce
# State 0 (button not pressed)
# State 1 (button released)
# State 2 (Debounce for X ms)
debounce_state = 0
# Time last read the gpio
last_read_gpio = None
# How many ms to wait before reading gpio again
gpio_debounce = 100

def triggerPush():
    # global keyword indicates that the variable is a global variable
    global last_read_gpio
    global debounce_state
    
    current_time = getTimeMS()
    
    if last_read_gpio is None:
        last_read_gpio = current_time
        
    time_delta = current_time - last_read_gpio

    # Read value of push button gpio
    # GPIO Code below
    btn_val =  getPushButtonVal()
    
    # Transition from state 0 to state 1 and set rtn_val= True
    # if the variable for state is equal to 0 and button has been pressed     
    # GPIO Code below
    if debounce_state == 0 and btn_val == 1:
        debounce_state = 1
        return True
   
    # Transition from state 1 to state 2 and set last_read_gpio to current_time
    # if the variable for state is equal to 1 and button has been released  
    # GPIO Code below
    elif debounce_state == 1 and btn_val == 0:
        debounce_state = 2
        last_read_gpio = current_time
        return False
        
    # Transition from state 2 to state 0
    # if the variable for state is equal to 2 and time_delta is greater than gpio_debounce
    # GPIO Code below
    elif debounce_state == 2 and  (time_delta) > gpio_debounce:
        debounce_state = 0
        return False
        
    return False


# Save the current ADC state machine value
# State 0: Ready to read ADC and trigger if threshold is met
# State 1: "Debounce" -> wait X ms before going back to state 1 after trigger
adc_cur_state = 0
# Get last value the ADC read
adc_last_val = -1
# Time the ADC was last read
last_read_adc = 0
# The value between current ADC and previous ADC value needed to trigger a twist
adc_threshold = 300
# Time in ms to wait before the twist action can be triggered again
adc_debounce = 500


def setADCBaseLine():
    global adc_last_val
    val = 3000
    # Read raw ADC value for pin connected to potentiometer and 
    # set the value to "val" variable
    # ADC Code below
    val = readPotentiometerVal() ## Solution

    if val is not 3000:
        adc_last_val = val
    
def triggerTwist():
    global adc_last_val
    global adc_cur_state
    global last_read_adc
    
    current_time = getTimeMS()
    time_delta = current_time-last_read_adc
    rtn_val = False
    cur_val = 0
    
    if adc_cur_state == 1 and (time_delta) > adc_debounce:
        setADCBaseLine()
        adc_cur_state = 0

    if adc_cur_state == 0:
        # Read voltage from potentiometer
        # ADC Code below
        cur_val = readPotentiometerVal() ## Solution
        val_delta = abs(adc_last_val-cur_val)
        
        if cur_val is not 3000 and abs(val_delta) > adc_threshold:
            adc_cur_state = 1
            last_read_adc = getTimeMS()
            rtn_val = True
    
    return rtn_val

# Sensor state machine
# State 0: Ready to be read. Trigger if blocked
# State 1: Waiting to be unblocked. Go to state 0 if unblocked
sensor_state = 0;
# Time since sensor was last read
last_read_sensor = None
blocked_threshold = 30
unblocked_threshold = 60

def triggerBlock():
    global last_read_sensor
    global sensor_state
    
    rtn_val = False
    current_time = getTimeMS()
    
    if last_read_sensor is None:
        last_read_sensor = current_time
        
    time_delta = current_time - last_read_sensor
    
    # Don't read sensor again unless TSL2561_DELAY_INTTIME_13MS has passed
    if (time_delta) > TSL2561_DELAY_INTTIME_13MS:

        val = getLightValue()
        
        if val is not -1 and sensor_state == 0 and val < blocked_threshold:
            rtn_val = True
            sensor_state = 1

        elif val is not -1 and sensor_state == 1 and val >= unblocked_threshold:
            sensor_state = 0
                    
    return rtn_val  
    
# Define a function for the thread
def processActions( threadName):
     global checked
     global response

     while True:
        new_val = "Nothing"

        if checked is True:
            setADCBaseLine()
            checked = False
            response = "Nothing"
        else:
            if triggerTwist():
                new_val = "ADC"
            elif triggerPush():
                new_val = "GPIO"
            elif triggerBlock():
                new_val = "BLOCK"

        if response is "Nothing":
            response = new_val
            if response is not "Nothing":
                print response


i2cSetup()
gpioSetup()
adcSetup()


# Create two threads as follows
try:
     thread.start_new_thread( processActions, ("Thread-1",  ) )

except:
     print "Error: unable to start thread"



# Define a function for the thread
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():

    global checked
    global response

    if checked is True:
        return "Nothing"

    if response is not "Nothing":
        checked = True

    return response

if __name__ == '__main__':
            app.run(host='0.0.0.0', port=12788)
