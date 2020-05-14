import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
while True:
    i=GPIO.input(11)
    if i==0:  
        print ("No intruder")
        time.sleep(0.1)
    elif i==1:  
        print("Intruder detected")
        time.sleep(0.1)
GPIO.cleanup()