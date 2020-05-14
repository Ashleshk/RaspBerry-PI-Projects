import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
for i in range(0,10):
    print("Relay on")
    GPIO.output(7,GPIO.HIGH)
    time.sleep(2)
    print("Relay off")
    GPIO.output(7,GPIO.LOW)
    time.sleep(2)
else:
    print("End")
GPIO.cleanup()
 