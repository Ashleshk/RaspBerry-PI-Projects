importRPi.GPIO as GPIO 
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(11,GPIO.OUT)
while True: 						# Run forever
	if GPIO.input(3) == GPIO.LOW:
		print("Button was pushed!")
		GPIO.output(11,True)
		time.sleep(1)
	elif GPIO.input(3) == GPIO.HIGH:
		print("Button is released!")
		GPIO.output(11,False)
		time.sleep(1)
GPIO.cleanup()
