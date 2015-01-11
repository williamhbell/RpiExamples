Simple LED control using GPIO
=============================
W. H. Bell

Overview
--------

This is a very simple example that uses the GPIO and the HumblePi 
breakout board.  The GPIO connections provide unprotected 3.3V logic 
that can be directly connected to some devices.  For this circuit, a 
LED is connected from one of the ground (GND) pins on the GPIO 
connector to a 330 Ohm resistor.  Each resistor is then connected to a 
GPIO pin.

Running the program
-------------------

Accessing the GPIO logic, rather than one of the buses on the GPIO 
connector, requires superuser access.  To run the program, type:

cd python
sudo ./LED.py

The sudo command is used to cause the process to run as the root user.

To stop the program, type

CTRL-C


The program
-----------

The GPIO port can be setup with GPIO.BOARD or GPIO.BCM numbering.  For 
this example, the BCM numbering scheme is used.  More details on the 
numbering scheme can be found at

http://elinux.org/RPi_Low-level_peripherals

There is one loop before the main loop, where each GPIO that is 
associated with a LED is set as an output connection.  In this loop, 
all of the LEDs are also set to be off.

The main loop is within a try-except statement.  The loop will continue 
forever unless the user types CTRL-C.  Typing CTRL-C causes the except 
part of the statement, which calls the GPIO clean up function to clear 
the associated memory.  Within the loop itself, the GPIO.output function is 
used to turn on or off the associated LED.  The sleep statements are 
used to allow the human eye to see the LED pattern produced.

Possible extensions
-------------------

 * Try modifying the LED pattern by modifying the LED loops.

 * Try coupling this example with the PIR example, to turn on or off 
   LEDs when someone passes by.
