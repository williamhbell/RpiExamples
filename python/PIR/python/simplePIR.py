#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

# A variable to store the GPIO associated with the PIR
pir = 24

# Set the numbering scheme to use the BCM scheme
GPIO.setmode(GPIO.BCM)

# Set the GPIO associated with the PIR to be an input
GPIO.setup(pir, GPIO.IN)

# Use a try-except statement to allow CTRL-C
try:

  print("Now checking the PIR.")
  print("Type CTRL-C to quit the loop.")

  while True:
    # Check the status of the PIR
    if GPIO.input(pir):
      print("The PIR has triggered")

    # Sleep for 1/2 a second, to prevent too many messages
    time.sleep(0.5)

# If someone presses CTRL-C, then clean up the GPIO
except KeyboardInterrupt:
  GPIO.cleanup()
