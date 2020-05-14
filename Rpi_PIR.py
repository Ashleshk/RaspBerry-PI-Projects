import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(11,GPIO.IN)
GPIO.setwarnings(False)

while 1:
 x=GPIO.input(11)
 if x==1:
	print "object detected"
    	GPIO.output(3,True)
	time.sleep(0.1)	
 elif x==0:
    	print "no object found"
    	GPIO.output(3,False)
	time.sleep(0.1)
GPIO.cleanup()
