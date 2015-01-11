#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

# Declare some variables to hold the GPIO numbers of the LEDs
red = 23 
green = 18
blue = 17
yellow = 4
leds = [ red, green, blue, yellow ]

# Number of seconds to wait
waitTime = 0.1

# Set the BCM numbering scheme for the GPIO
GPIO.setmode(GPIO.BCM)

# Set all of the GPIO pins for the LEDs as output pins
# and make sure that they are off
for led in leds:
  GPIO.setup(led,GPIO.OUT) # Set the GPIO as an output connection
  GPIO.output(led,0)  # Switch the LED off

# Use a try-except statement to allow CTRL-C
try:

  print("Now looping through the LEDs.")
  print("Type CTRL-C to quit the loop")

  # Now cycle through the colours
  while True:
    for led in leds:
      GPIO.output(led,1) # Switch the LED on
      time.sleep(waitTime) # Wait to allow the colour to be seen
    for led in leds:
      GPIO.output(led,0) # Switch the LED off
      time.sleep(waitTime) # Wait to allow the eye to notice

# If someone presses CTRL-C, then clean up the GPIO
except KeyboardInterrupt:
  GPIO.cleanup()
