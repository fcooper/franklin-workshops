# This is how you create a comment in python

# Python equivalent of include statement
import time

# Statements require no semicolon at the end
# You don't specify a datatype for a variable
franklin = "Texas Instruments"

# print statement in python
print (franklin)

# You can reassign a variable any datatype you want
# this will make the variable a decimal
franklin = 1.0

# You can concatnate seperate strings by adding the + symbol between them
# To convert a number to a string use the str function
print ("Printing number " + str(franklin))

# If statements end with colon
if franklin == 1.0:
	# Lines under a if statement, loop or function must be indented.
	# The indentation mimics what curly brackets are used for in other languages
	print("Franklin equals 1.0")

# Syntax for else if. Also includes colon
elif franklin == 2.0:
	print("Franklin equals 2.0")

# Syntax for else statement. Also includes colon
else:
	print("Unknock value for Franklin")

# Its True and False. TRUE/FALSE or true/false will not work
if True == True:
	print ("True is indeed True")

if False == False:
	print ("False is indeed False")