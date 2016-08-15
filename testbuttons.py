import time
import RPi.GPIO as GPIO

switch1 = 17
switch2 = 26

GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

print "start"

while True:
    if not GPIO.input(switch1):
        print "Button 1 pressed"
        time.sleep(0.5)
            
    elif not GPIO.input(switch2):
        print "Button 2 pressed"
        time.sleep(0.5)
     
    else:
        pass