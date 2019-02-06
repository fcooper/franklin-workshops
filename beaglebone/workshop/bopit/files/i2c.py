#!/usr/bin/python

# Texas Instruments Created Library
import workshop

# External Helper Libraries
# import required i2c/smbus library
## PUT YOUR CODE HERE ##

#Standard Python Library
import time


def convertToU16(value,little_endian=True):
	value = value & 0xFFFF
	
	if not little_endian:
		value = ((value << 8) & 0xFF00) + (value >> 8)
	return value
	
# I2C

# Configure Pinmux First
# Set both P9_19 and P9_20 pin's pinmux to i2c mode
## PUT YOUR CODE HERE ##
## PUT YOUR CODE HERE ##

#Initialize I2C/smbus to the 2nd i2c instance. Set the value returned by the function to the "bus" variable
## PUT YOUR CODE HERE ##


# I2C address options
TSL2561_I2C_ADDR          = (0x29)    # Default address (pin left floating)

TSL2561_COMMAND_BIT         = (0x80)    # Must be 1
TSL2561_WORD_BIT            = (0x20)    # 1 = read/write word (rather than byte)

TSL2561_CONTROL_POWERON     = (0x03)
TSL2561_CONTROL_POWEROFF    = (0x00)

TSL2561_REGISTER_CONTROL    = 0x00

TSL2561_DELAY_INTTIME_13MS  = (15) / 1000
TSL2561_REGISTER_CHAN0_LOW  = 0x0C

# Power Device Off
# using a function to write a byte of data via smbus
# set address parameter  to: TSL2561_I2C_ADDR
# set command parameter  to: (TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL)
# set function parameter to: TSL2561_CONTROL_POWEROFF
# Use the below syntax. Replace what is in the <> with the proper text
# syntax:
# bus.<function>(<i2c address>, <command param>, <function param>)
## PUT YOUR CODE HERE ##


#Wait 1 Sec
time.sleep(1)

# Power Device ON
# use a function to write a byte of data via smbus
# set address parameter  to: TSL2561_I2C_ADDR
# set command parameter  to: (TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL)
# set function parameter to: TSL2561_CONTROL_POWERON
# Use the below syntax. Replace what is in the <> with the proper text
# syntax:
# bus.<function>(<i2c address>, <command param>, <function param>)
## PUT YOUR CODE HERE ##



val = 0
while True:

	# Read I2C device's light intensity value and set the value returned to "val" variable.
	# use a function to read a word of data via smbus
	# set address parameter  to: TSL2561_I2C_ADDR
	# set command parameter  to: (TSL2561_COMMAND_BIT | TSL2561_WORD_BIT | TSL2561_REGISTER_CHAN0_LOW)
	# Use the below syntax. Replace what is in the <> with the proper text
	# syntax:
	# bus.<function>(<i2c address>, <command param>, <function param>)
	## PUT YOUR CODE HERE ##


	# Convert "val" variable to unsigned 16
	val = convertToU16(val)

	# Sleep for "TSL2561_DELAY_INTTIME_13MS"
	## PUT YOUR CODE HERE ##


	print val
	time.sleep(1)
