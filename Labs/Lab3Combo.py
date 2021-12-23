#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

TRIG = 11
ECHO = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.output(TRIG, GPIO.HIGH)


def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	while True:
		dis = distance()
		print (int(dis), 'cm')
		print ('')
		if dis < 20:
			beep(0.5)
		off()
		time.sleep(0.5)
def on():
        GPIO.output(TRIG, GPIO.LOW)

def off():
        GPIO.output(TRIG, GPIO.HIGH)

def beep(x):
        on()
        time.sleep(x)
        off()
        time.sleep(x)

def destroy():
        GPIO.output(TRIG, GPIO.HIGH)
        GPIO.cleanup()

if __name__ == "__main__":
	setup()
	off()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
