import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
pin = [13, 11, 3]
i = 0
prePin = pin[0]
cp = pin[0]
while True:
    input("Press enter")
    GPIO.output(11, False)
    GPIO.output(3, False)
    GPIO.output(13, False)
    GPIO.output(pin[i], True)
    i+=1
    if i > 2:
        i = 0