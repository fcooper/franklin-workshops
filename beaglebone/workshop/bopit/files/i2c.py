#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
import smbus

#Standard Python Library
import time


def convertToU16(value,little_endian=True):
    value = value & 0xFFFF
    
    if not little_endian:
        value = ((value << 8) & 0xFF00) + (value >> 8)
    return value
    
# I2C

#Configure Pinmux First
# Set correct pins pinmux to i2c mode
# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!

#Initialize I2C/smbus to the correct i2c instance
# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!

# I2C address options
TSL2561_I2C_ADDR          = (0x29)    # Default address (pin left floating)

TSL2561_COMMAND_BIT         = (0x80)    # Must be 1
TSL2561_WORD_BIT            = (0x20)    # 1 = read/write word (rather than byte)

TSL2561_CONTROL_POWERON     = (0x03)
TSL2561_CONTROL_POWEROFF    = (0x00)

TSL2561_REGISTER_CONTROL    = 0x00

TSL2561_DELAY_INTTIME_13MS  = (15) / 1000
TSL2561_REGISTER_CHAN0_LOW  = 0x0C

#Power Device Off (Set back to default configuration)
# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!

#Wait 1 Sec
time.sleep(1)

#Power Device ON
# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!


val = 0
while True:
	# Read word (16 bits) at memory location (TSL2561_COMMAND_BIT | TSL2561_WORD_BIT | TSL2561_REGISTER_CHAN0_LOW)
	# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!

	#Convert value you read to unsigned 16
	# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!

	#Sleep for TSL2561_DELAY_INTTIME_13MS
	# !!!!!!!!!!!!!!!!! ADD YOUR CODE HERE !!!!!!!!!!!!!!!!!


	print val
	time.sleep(1)
