import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
# a/e
while True:
    ae = input("e - licht ein, a - licht aus")
    if ae == "e":
        GPIO.output(3, True)
    elif ae == "a":
        GPIO.output(3, False)