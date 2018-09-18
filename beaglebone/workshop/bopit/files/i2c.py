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

#Configure Pinmux First
# Set both P9_19 and P9_20 pin's pinmux to i2c mode
## PUT YOUR CODE HERE ##
## PUT YOUR CODE HERE ##

#Initialize I2C/smbus to the correct i2c instance
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

# Power Device Off (Set back to default configuration)
# using function to write byte of data via smbus
# set function command to: (TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL)
# set function value to: TSL2561_CONTROL_POWEROFF
# set function address to: TSL2561_I2C_ADDR
## PUT YOUR CODE HERE ##


#Wait 1 Sec
time.sleep(1)

# Power Device ON
# using function to write byte of data via smbus
# set function command to: (TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL)
# set function value to: TSL2561_CONTROL_POWERON
# set function address to: TSL2561_I2C_ADDR
## PUT YOUR CODE HERE ##



val = 0
while True:
	# Read I2C device's light intensity value.
	# using function to read word worth of data via smbus
	# set function command to: (TSL2561_COMMAND_BIT | TSL2561_WORD_BIT | TSL2561_REGISTER_CHAN0_LOW)
	# set function address to: TSL2561_I2C_ADDR
	## PUT YOUR CODE HERE ##


	#Convert value you read to unsigned 16
	val = convertToU16(val)

	#Sleep for TSL2561_DELAY_INTTIME_13MS
	## PUT YOUR CODE HERE ##


	print val
	time.sleep(1)
