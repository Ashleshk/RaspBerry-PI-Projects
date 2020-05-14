import RPi.GPIO as GPIO
from time import sleep
import sys

#assign GPIO pins for motor
motor_channel = (29,31,33,35)  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#for defining more than 1 GPIO channel as input/output use
GPIO.setup(motor_channel, GPIO.OUT)

motor_direction=input('1=Clockwise and 0=Anti-Clockwise')                                                    
while True:
	try:
		 if(motor_direction==0):
			print('motor running anti-clockwise\n')
                		GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
                		sleep(0.02)
                		GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
               			 sleep(0.02)
                		GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
                		sleep(0.02)
                		GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
                		sleep(0.02)

        		elif(motor_direction==1):
            			print('motor running clockwise\n')
            			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
            			sleep(0.02)
            			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
            			sleep(0.02)
            			GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
           			 sleep(0.02)
            			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
            			sleep(0.02)


	#press ctrl+c for keyboard interrupt
	except KeyboardInterrupt:
       	 #query for setting motor direction or exit
        		motor_direction = input('select motor direction a=anticlockwise, c=clockwise or q=exit: ')
        		#check for exit
        		if(motor_direction == 'q'):
           			 print('motor stopped')
            			sys.exit(0)
