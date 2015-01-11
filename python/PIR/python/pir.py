#!/usr/bin/python
 
import RPi.GPIO as GPIO
import time
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PIR = 7
 
print "PIR Module Test (CTRL-C to exit)"
 
# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
 
Current_State  = 0
Previous_State = 0
 
try:
 
  print "Waiting for PIR to settle ..."
 
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0
 
  print "  Ready"
 
  # Taper CTRL-C pour quitter
  while True :
 
    # Lire le PIR
    status = GPIO.input(GPIO_PIR)
 
    if status == 1 and Previous_State == 0:
      # PIR is triggered
      print "  Motion detected!"
      # Record previous state
      Previous_State = 1
    elif status == 0 and Previous_State == 1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0
 
    # Wait for 10 milliseconds
    time.sleep(0.01)
 
except KeyboardInterrupt:
  print " Nous sommes sorties"
  # Nettoyez le GPIO
  GPIO.cleanup()
