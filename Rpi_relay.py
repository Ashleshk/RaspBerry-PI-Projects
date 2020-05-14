import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)

for i in range (0,56):
	print "Relay on"
       	GPIO.output(11,True)
       	time.sleep(2)

       	print "Relay off"
       	GPIO.output(11,False)
       	time.sleep(2)

print "END"
GPIO.cleanup()