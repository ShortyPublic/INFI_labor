import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
# Lang/Kurz/Lang
while True:
    GPIO.output(3, True)
    time.sleep(1)
    GPIO.output(3, False)
    time.sleep(0.3)
    GPIO.output(3, True)
    time.sleep(0.3)
    GPIO.output(3, False)
    time.sleep(0.3)