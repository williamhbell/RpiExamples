PIR motion sensor
=================
W. H. Bell

Overview
--------

Passive infrared (PIR) sensors are available in cheap formats,  
http://www.tandyonline.co.uk/pir-motion-sensor-module.html

which can be powered by the 5V output of the GPIO and provide a 3.3V 
logic output that can be directly connected to a Raspberry Pi GPIO pin.  
There are two screw adjusters on the PIR board that allow the 
sensitivity of the PIR and the length of the output pulse to be 
modified.

simplePIR
---------

Type

sudo ./simplePIR.py

to run the program.  This program checks to see if the PIR is sending a 
high signal, but does not check if the PIR has settled in between or 
after the trigger.


highAndLowPIR
-------------

Type

sudo ./highAndLowPIR.py

to run the example.  The program uses a tight loop to check if the PIR 
has settled or has triggered.  The current and previous state is used 
to check the current state of the PIR and find a trigger.

Interrupts
----------

Type

sudo ./interrupts.py

to run the example.  The program uses an interrup to check if the PIR signal
goes high.  This means the CPU is idle until the PIR signal goes high.

Extensions
----------

  * Try combining the PIR status with one or more LEDs.
