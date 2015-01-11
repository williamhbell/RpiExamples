#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

# Define two call back functions to be called when the status of the 
# PIR changes
def callback_up(channel):
  print('Up detected on channel %s' % channel)

def callback_down(channel):
  print('Down detected on channel %s' % channel)

# A variable to store the GPIO associated with the PIR
pir = 24

# Set the numbering scheme to use the BCM scheme
GPIO.setmode(GPIO.BCM)

# Set the GPIO associated with the PIR to be an input
GPIO.setup(pir, GPIO.IN)

try:
  print("Adding the interrupt and waiting for CTRL-C or PIR signal")

  # Add an interrupt that will call the callback_up function when the 
  # PIR goes high
  # (GPIO.RISING or GPIO.FALLING or GPIO.BOTH are allowed.)
  GPIO.add_event_detect(pir, GPIO.RISING, callback=callback_up)

  # Can try this instead
  #GPIO.add_event_detect(pir, GPIO.FALLING, callback=callback_down)

  # Sleep forever, to keep the program running
  while True:
    time.sleep(100)

# If someone presses CTRL-C, then clean up the GPIO
except KeyboardInterrupt:
  GPIO.cleanup()
