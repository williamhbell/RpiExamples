Running the examples

Open terminal window

cd rpi_sensor_board

Accelerometer

sudo python accelerometer.py

And set the pendulum going. 

We're just focusing on the two axes that change the most

Temperature

sudo python temperature.py

And put your finger on the the silvery MPL sensor to change the temp.

Initial Setup:

From Element14 manual:

After logging into RPi, edit /etc/modprobe.d/raspi-blacklist.conf by typing:

$ sudo nano /etc/modprobe.d/raspi-blacklist.conf

Insert a hash(#) at the start of the line blacklist i2c-bcm2708, it should be read:

Type in a terminal:

$ sudo modprobe i2c-bcm2708

Next, you need to install the sensor drivers. Download the driver and python test scripts from:

git clone http://git.oschina.net/embest/rpi_sensor_board.git

When the downloading finished, reboot your Raspberry Pi:

References:

http://goughlui.com/2014/06/30/getting-started-freescale-xtrinisic-sense-board-on-rpi-kl-25z/
http://www.raspberrypi-spy.co.uk/2014/06/farnell-xtrinsic-mems-sensor-board-for-raspberry-pi/
http://www.element14.com/community/docs/DOC-65084/l/xtrinsic-sensor-board
https://github.com/larsch/rpi-mems-sensor
http://www.farnell.com/datasheets/1804142.pdf