import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(3,IO.OUT) 			#pin 3(GPIO 2) ->  LED as output
IO.setup(11,IO.IN) 				#pin 11(GPIO 17) -> IR sensor as input
while 1:
	if(IO.input(11)==True):		 #object is far away
        		print "not Detected"
        		IO.output(3,False)		 # led OFF    
    	elif(IO.input(11)==False): 		#object is near
        		print " Detected"
       	 	IO.output(3,True) 		#led ON
GPIO.cleanup()        
       