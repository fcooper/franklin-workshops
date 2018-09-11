import subprocess
import re

def getPinMux(pin_name):

	# Make sure that the pin name passed appears to be valid
	result = re.match("^P[89]{1}_[0-9]{1,2}$", pin_name)

	if result is None:
		print "Invalid Pin Name Format"
		return False

	cmd = "config-pin -l "+pin_name

	try:
		returned_output = subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT)
	except subprocess.CalledProcessError, e:
		print e.output
		return False

	return returned_output.strip().split(" ")

def setPinMux(pin_name,mode):

	valid_modes = getPinMux(pin_name)
	if valid_modes is False:
		return False

	if mode not in valid_modes:
		print "Not a valid mode for this pin"
		return False

	cmd = "config-pin "+pin_name+" "+mode

	try:
		returned_output = subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT)
	except subprocess.CalledProcessError, e:
		print e.output
		return False

	return True
