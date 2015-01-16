Robotic Arm
===========
Author: W. H. Bell

Overview
--------

The Maplin (OWI) robotic arm comes as a kit that includes a USB 
controller.  The robotic arm can be directly connected to a Raspberry 
Pi, where the electrical power for the five motors and the LED is 
provided by batteries in the base.  To connect to the robotic arm, the 
robotic arm should be turned on using the power switch on top of the 
unit and the USB should be connected.  If the motors are driven for too 
long, the gears will start to crunch.  If this happens, turn the 
robotic arm power off immediately and then correct the program.



Software dependencies
---------------------

To install the software dependencies for the robotic arm type:

sudo -s
apt-get install -y python-setuptools python-dev
easy_install pip
pip install pyusb
exit

This software has already been installed on the Raspberry Pi connected 
to the robotic arm.
