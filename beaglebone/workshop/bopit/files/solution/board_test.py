#!/usr/bin/python

import workshop
import smbus  ## Solution
import time

import Adafruit_BBIO.ADC as ADC 
import Adafruit_BBIO.GPIO as GPIO

from flask import Flask

from flask_cors import CORS

def convertToU16(value,little_endian=True):
	value = value & 0xFFFF
	
	if not little_endian:
		value = ((value << 8) & 0xFF00) + (value >> 8)
	return value

workshop.setPinMux("P9_29","gpio")
workshop.setPinMux("P9_19","i2c")
workshop.setPinMux("P9_20","i2c")
GPIO.setup("P9_29", GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


ADC.setup()


bus = smbus.SMBus(2) ## Solution


TSL2561_I2C_ADDR          = (0x29)    # Default address (pin left floating)

TSL2561_COMMAND_BIT         = (0x80)    # Must be 1
TSL2561_WORD_BIT            = (0x20)    # 1 = read/write word (rather than byte)

TSL2561_CONTROL_POWERON     = (0x03)
TSL2561_CONTROL_POWEROFF    = (0x00)

TSL2561_REGISTER_CONTROL    = 0x00

TSL2561_DELAY_INTTIME_13MS  = (15) / 1000
TSL2561_REGISTER_CHAN0_LOW  = 0x0C

bus.write_byte_data(TSL2561_I2C_ADDR,TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL, TSL2561_CONTROL_POWEROFF) ## Solution


time.sleep(1)

bus.write_byte_data(TSL2561_I2C_ADDR, TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL, TSL2561_CONTROL_POWERON) ## Solution


count = 0
val = 0

print "Verifying that light sensor works. Move your hand up and down above the light sensor"
print "This will run for 6 seconds"

light = -1
status = False
while count < 12:
	val = bus.read_word_data(TSL2561_I2C_ADDR,TSL2561_COMMAND_BIT | TSL2561_WORD_BIT | TSL2561_REGISTER_CHAN0_LOW) ## Solution
	val = convertToU16(val)
	
	if light is -1 and val != 0:
		light = val
		
	time.sleep(TSL2561_DELAY_INTTIME_13MS)
	
	if abs(light - val) > 50:
		status = True
		
	time.sleep(.5)
	count = count + 1

if status is True:
	print "Light test has passed"
else:
	print "Light test has failed"
	

print "Push the push button"
while True:
	if GPIO.input("P9_29"):
		print "Push button test passed"
		break


pot = -1
status = False
print "Turn the potentiometer"
print "The value will very as you turn it"
print "This test will run for 5 seconds"
count = 0
while count < 5:
	val = ADC.read("P9_36")
	val = val * 1.8
	
	if pot is -1:
		pot = val
		
	if abs(pot-val) > .2:
		status = True
		
	time.sleep(1)
	count = count + 1
	
if status is True:
	print "potentiometer test has passed"
else:
	print "potentiometer test has failed"
	
