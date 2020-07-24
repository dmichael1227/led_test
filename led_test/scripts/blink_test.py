'''
Based on code found at https://raspberrypihq.com/making-a-led-blink-using-
the-raspberry-pi-and-python/
'''
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
print("Blinking!")
x=0
while x < 3:
    x = x + 1 
    GPIO.output(8, GPIO.HIGH)
    sleep(1)
    GPIO.output(8, GPIO.LOW)
    sleep(1)
