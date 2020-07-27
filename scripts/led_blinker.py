'''
Script based on https://raspberrypihq.com/making-a-led-blink-using-the-
raspberry-pi-and-python/
'''
import RPi.GPIO as GPIO
import sys
import getopt
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

print('Argument List: %s' % sys.argv)
if sys.argv[1] == "True":
    GPIO.output(8, GPIO.HIGH)
elif sys.argv[1] == "False":
    GPIO.output(8,GPIO.LOW)
else:
    print("ERROR: EXPECTING BOOL VALUE")
