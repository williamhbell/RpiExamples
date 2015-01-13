#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

# A variable to store the GPIO associated with the PIR
pir = 17

# Set the numbering scheme to use the BCM scheme
GPIO.setmode(GPIO.BCM)

# Set the GPIO associated with the PIR to be an input
GPIO.setup(pir, GPIO.IN)

# Variables to store the state of the PIR
currentState = 0
previousState = 0

# Use a try-except statement to allow CTRL-C
try:
  print("Type CTRL-C to quit the loop.")
  print("Waiting for PIR to settle ...")
 
  # Loop until PIR output is 0
  while GPIO.input(pir) == 1:
    currentState  = 0
 
  print(">> Ready")
 
  while True : 

    # Read the PIR status
    status = GPIO.input(pir)
 
    if status == 1 and previousState == 0:
      # PIR has triggered
      print(">> Motion detected!")

      # Record previous state
      previousState = 1
    elif status == 0 and previousState == 1:
      # PIR has returned to ready state
      print(">> Ready")
      previousState=0
 
    # Wait for 10 milliseconds.
    # (This causes a very tight loop, where an interupt would probably be a 
    # better solution.)
    time.sleep(0.01)

# If someone presses CTRL-C, then clean up the GPIO
except KeyboardInterrupt:
  GPIO.cleanup()
