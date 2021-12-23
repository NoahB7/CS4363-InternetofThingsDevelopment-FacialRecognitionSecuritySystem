#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

BtnPin = 11
Gpin   = 13
Rpin   = 12

def setup():
	print("setup method called")
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
	GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)

def loop():
	print("loop method called")
	while True:
		print("printing loop")
		GPIO.output(Rpin,1)
		time.sleep(3)
		GPIO.output(Gpin,0)
		GPIO.output(Rpin,0)
		time.sleep(1)

def destroy():
	print("destroy method called")
	GPIO.output(Gpin, GPIO.HIGH)       # Green led off
	GPIO.output(Rpin, GPIO.HIGH)       # Red led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

