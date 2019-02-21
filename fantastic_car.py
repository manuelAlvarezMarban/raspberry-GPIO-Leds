#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin0 =  6
LedPin1 =  5
LedPin2 =  11
LedPin3 =  9
LedPin4  = 10
LedPin5  = 22
LedPin6 =  17
LedPin7 =  24
LedPinPulsador = 13
chan_list = [6,5,11,9,10,22,17,24]

def setup():
        GPIO.setmode(GPIO.BCM)                                           
        GPIO.setup(chan_list, GPIO.OUT)
	GPIO.setup(LedPinPulsador,GPIO.IN)                                
        GPIO.output(chan_list, GPIO.LOW)                                    

def loop():
        while True:
		if GPIO.event_detected(LedPinPulsador):
			print "El Coche Fantastico"

                GPIO.output(LedPin0, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(LedPin1, GPIO.HIGH)  
                time.sleep(0.1)
                GPIO.output(LedPin2, GPIO.HIGH)  
                time.sleep(0.1)
                GPIO.output(LedPin3, GPIO.HIGH)  
                time.sleep(0.1)
                GPIO.output(LedPin4, GPIO.HIGH)  
                time.sleep(0.1)
                GPIO.output(LedPin5, GPIO.HIGH)  
                time.sleep(0.1)
                GPIO.output(LedPin6, GPIO.HIGH)  
                time.sleep(0.1)
                GPIO.output(LedPin7, GPIO.HIGH)  
              
                time.sleep(0.4)
                GPIO.output(LedPin7, GPIO.LOW)
                time.sleep(0.1)    
                GPIO.output(LedPin6, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(LedPin5, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(LedPin4, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(LedPin3, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(LedPin2, GPIO.LOW)
                time.sleep(0.1)  
                GPIO.output(LedPin1, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(LedPin0, GPIO.LOW) 
                time.sleep(0.7)



def destroy ():
        GPIO.output(chan_list, GPIO.LOW)            
        GPIO.cleanup()
if __name__ ==  '__main__':                              
        setup()
        try:
		GPIO.add_event_detect(LedPinPulsador,GPIO.RISING)
                loop()
	
        except KeyboardInterrupt:  
        # Capturar 'Ctrl+C' 
                destroy()

